from __future__ import annotations

import json
import os
import secrets
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

import ibis
import ibis.expr.types as ir
from ibis import Schema
from ibis.backends.base import BaseBackend
from ibis.backends.bigquery import Backend as BigQueryBackend
from ibis.backends.duckdb import Backend as DuckDBBackend
from ibis.backends.postgres import Backend as PostgresBackend
from tqdm import tqdm

from vinyl.lib.utils.pkg import _get_project_directory
from vinyl.lib.utils.text import _extract_uri_scheme

_TEMP_PATH_PREFIX = "vinyl_"


@dataclass
class SourceInfo:
    _name: str
    _location: str
    _schema: Schema | None
    _parent_resource: Any | None = None


class _ResourceConnector(ABC):
    """Base interface for handling connecting to resource and getting sources"""

    @abstractmethod
    def _list_sources(self, with_schema=False) -> list[SourceInfo]:
        pass

    @abstractmethod
    def _connect(self) -> BaseBackend:
        pass


# exists to help distinguish between table and database connectors
class _TableConnector(_ResourceConnector):
    _tbls: dict[str, ir.Table]
    _path: str

    def __init__(self, path: str):
        self._path = path

    def _get_table(self, path) -> ir.Table:
        # for file connectors, we reconnect to the individual file to get the correct table. Since these tables are not in memory, we need to read to get the location.
        adj_conn = self.__class__(path)
        adj_conn._connect()
        return next(iter(adj_conn._tbls.values()))

    def _generate_twin(self, path, sample_row_count=1000) -> ir.Table:
        tbl = self._get_table(path)
        row_count = tbl.count()
        sampled = tbl.filter(
            ibis.random() < ibis.least(sample_row_count / row_count, 1)
        )
        return sampled


class _DatabaseConnector(_ResourceConnector):
    _conn: BaseBackend
    _allows_multiple_databases: bool = True
    _tables: list[str]
    _excluded_dbs: list[str] = []
    _excluded_schemas: list[str] = []

    def _find_sources_in_db(
        self,
        databases_override: list[str] | None = None,
        with_schema: bool = False,
    ):
        self._connect()

        sources = []
        preprocess = []

        # get tables
        for loc in self._tables:
            database, schema, table = loc.split(".")
            if databases_override is not None:
                adj_databases = databases_override
            elif database == "*":
                if not hasattr(self._conn, "list_databases"):
                    raise ValueError(
                        f"Database specification required for this connector: {self.__class__.__name__}"
                    )
                adj_databases = list(
                    set(self._conn.list_databases()) - set(self._excluded_dbs)
                )
            else:
                adj_databases = [database]

            for db in adj_databases:
                if schema == "*":
                    schema_set = set(
                        self._conn.list_schemas(database=db)
                        if self._allows_multiple_databases
                        else self._conn.list_schemas()
                    )
                    adj_schemas = list(schema_set - set(self._excluded_schemas))
                else:
                    adj_schemas = [schema]
                for sch in adj_schemas:
                    if table == "*":
                        table_set = set(
                            self._conn.list_tables(database=db, schema=sch)
                            if self._allows_multiple_databases
                            else self._conn.list_tables(schema=sch)
                        )
                        adj_tables = list(table_set)
                    else:
                        adj_tables = [table]

                    for tbl in adj_tables:
                        preprocess.append((db, sch, tbl))
        msg = (
            "generating source schemas... "
            if len(preprocess) > 1
            else "generating source schema... "
        )
        for pre in tqdm(preprocess, msg):
            db, sch, tbl = pre
            location = f"{db}.{sch}"
            if with_schema:
                if self._allows_multiple_databases:
                    ibis_table = self._conn.table(database=db, schema=sch, name=tbl)
                else:
                    ibis_table = self._conn.table(schema=sch, name=tbl)
                schema = ibis_table.schema()
            sources.append(
                SourceInfo(
                    _name=tbl,
                    _location=location,
                    _schema=(ibis_table.schema() if with_schema else None),
                )
            )

        return sources

    @classmethod
    def _create_twin_connection(cls, path: str) -> DuckDBBackend:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        return ibis.duckdb.connect(path)

    def _get_table(self, database: str, schema: str, table: str) -> ir.Table:
        conn = self._connect()
        return conn.table(database=database, schema=schema, name=table)

    def _generate_twin(
        self,
        twin_path: str,
        database: str,
        schema: str,
        table: str,
        sample_row_count: int | None = 1000,
    ) -> ir.Table:
        tbl = self._get_table(database, schema, table)
        if sample_row_count is None:
            sampled = tbl
        else:
            row_count = tbl.count()
            # using safer random() sample
            sampled = tbl.filter(
                ibis.random() < ibis.least(sample_row_count / row_count, 1)
            )
        pyarrow_table = sampled.to_pyarrow()
        conn = self._create_twin_connection(twin_path)
        # using raw sql to set the schema since the argument is not supported in the ibis api

        # create final table
        conn.raw_sql(f"CREATE SCHEMA IF NOT EXISTS {schema}")
        conn.raw_sql(f"USE {schema}")
        table_temp_name = f"table_{secrets.token_hex(8)}"
        temp_table = conn.create_table(
            table_temp_name, obj=pyarrow_table, overwrite=True
        )

        # reconnect to catch type errors
        reconn = ibis.duckdb.connect(twin_path)
        temp_table = reconn.table(table_temp_name, schema=schema)
        original_types = sampled.schema().types
        cast_dict = {}
        for i, (name, type) in enumerate(temp_table.schema().items()):
            cast_dict[name] = original_types[i]
        temp_table = temp_table.cast(cast_dict)

        # create final table and delete temp one
        final_table = conn.create_table(table, obj=temp_table, overwrite=True)
        conn.drop_table(table_temp_name)
        return final_table


class _FileConnector(_ResourceConnector):
    _conn: DuckDBBackend = ibis.duckdb.connect()
    _paths_visited: list[str] = []
    _excluded_dbs = ["system", "temp"]
    _excluded_schemas = ["information_schema", "pg_catalog"]
    _remote: bool
    _path: str

    def __init__(self, path: str):
        if scheme := _extract_uri_scheme(path):
            import fsspec

            self._conn.register_filesystem(fsspec.filesystem(scheme))
            self._remote = True
            self._path = path
        else:
            self._remote = False
            # adjust local path so it works even if you are not in the root directory
            self._path = os.path.join(_get_project_directory(), path)


class DatabaseFileConnector(_FileConnector, _DatabaseConnector):
    def __init__(self, path: str, tables: list[str] = ["*.*.*"]):
        super().__init__(
            path
        )  # init method from _FileConnector, not Database Connector (because of ordering)
        self._tables = tables
        if any([len(t.split(".")) != 3 for t in tables]):
            raise ValueError(
                "tables must be a string of format 'database.schema.table'"
            )

    def _list_sources(self, with_schema=False) -> list[SourceInfo]:
        out = self._find_sources_in_db(with_schema=with_schema)
        return out

    def _connect(self) -> DuckDBBackend:
        return self._connect_helper(self._conn, self._path)

    @classmethod
    @lru_cache()
    def _connect_helper(cls, conn, path) -> DuckDBBackend:
        # caching ensures we don't attach a database from the same path twice
        if path.endswith(".duckdb"):
            name = cls._get_db_name(path)
            conn.attach(path, name)

        else:
            raise NotImplementedError(
                f"Connection for {path} not supported. Only .duckdb files are supported"
            )
        return conn

    @property
    def _database(self) -> str:
        return self._get_db_name(self._path)

    @classmethod
    @lru_cache()
    def _get_db_name(cls, path):
        name = Path(path).stem
        # handle situation where two database files have the same stem name
        if name in cls._conn.list_databases():
            name += str(secrets.token_hex(8))
        return name


class FileConnector(_FileConnector, _TableConnector):
    _tbls: dict[str, ir.Table]

    def __init__(self, path: str):
        super().__init__(
            path
        )  # init method from _FileConnector, not Database Connector (because of ordering)
        self._tbls: dict[str, ir.Table] = {}

    def _connect(self) -> DuckDBBackend:
        # caching ensures we don't attach a database from the same path twice
        self._tbls = self._connect_helper(self._conn, self._path)
        return self._conn

    def _list_sources(self, with_schema=False) -> list[SourceInfo]:
        self._connect()
        return [
            SourceInfo(
                _name=tbl.get_name(),
                _location=path,
                _schema=tbl.schema() if with_schema else None,
            )
            for path, tbl in self._tbls.items()
        ]

    @classmethod
    @lru_cache()
    def _connect_helper(cls, conn, path) -> dict[str, ir.Table]:
        stem = Path(path).stem
        tbls = {}
        # caching ensures we don't attach a database from the same path twice
        if path.endswith(".csv"):
            tbls[path] = conn.read_csv(path, table_name=stem)
        elif path.endswith(".parquet"):
            tbls[path] = conn.read_parquet(path, table_name=stem)
        elif path.endswith(".json"):
            tbls[path] = conn.read_json(path, table_name=stem)
        elif os.path.isdir(path):
            for sub in os.listdir(path):
                path_it = os.path.join(path, sub)
                # only looking at files prevents recursion into subdirectories
                if os.path.isfile(path_it) and not sub.startswith("."):
                    tbls.update(cls._connect_helper(conn, path_it))

        else:
            raise NotImplementedError(
                f"Connection for {path} not supported. Only .csv, .parquet, and .json files are supported"
            )

        return tbls


class BigQueryConnector(_DatabaseConnector):
    _credentials: Any

    def __init__(
        self,
        tables: list[str],
        service_account_path: str | None = None,
        service_account_info: str | None = None,
    ):
        from google.oauth2 import service_account

        if service_account_path is not None:
            credentials = service_account.Credentials.from_service_account_file(
                service_account_path
            )
        elif service_account_info is not None:
            credentials = service_account.Credentials.from_service_account_info(
                json.loads(service_account_info)
            )
        else:
            credentials = None

        self._credentials = credentials
        self._tables = tables

    def _connect(self) -> BigQueryBackend:
        self._conn = BigQueryConnector._connect_helper(self._credentials)
        return self._conn

    def _list_sources(self, with_schema=False) -> list[SourceInfo]:
        self._connect()
        return self._find_sources_in_db(with_schema=with_schema)

    # caching ensures we create one bq connection per set of credentials across instances of the class
    @staticmethod
    @lru_cache()
    def _connect_helper(credentials) -> BigQueryBackend:
        return ibis.bigquery.connect(credentials=credentials)


class PostgresConnector(_DatabaseConnector):
    _excluded_schemas = [
        "information_schema",
        "pg_catalog",
        "pgsodium",
        "auth",
        "extensions",
        "net",
    ]
    _allows_multiple_databases: bool = False
    _host: str
    _port: int
    _user: str
    _password: str
    _database: str

    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        tables: list[str],
    ):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._tables = tables

        # postgres requires connecting at the database level
        dbs = set([t.split(".")[0] for t in tables])
        if len(dbs) > 1 or "*" in dbs:
            raise ValueError("Postgres connector only supports one database at a time")
        self._database = dbs.pop()

    def _connect(self) -> PostgresBackend:
        self._conn = self._connect_helper(
            self._host, self._port, self._user, self._password, self._database
        )
        return self._conn

    def _list_sources(self, with_schema=False) -> list[SourceInfo]:
        self._connect()
        return self._find_sources_in_db(with_schema=with_schema)

    # caching ensures we create one bq connection per set of credentials across instances of the class
    @staticmethod
    @lru_cache()
    def _connect_helper(
        host: str, port: int, user: str, password: str, database: str
    ) -> PostgresBackend:
        return ibis.postgres.connect(
            host=host, port=port, user=user, password=password, database=database
        )
