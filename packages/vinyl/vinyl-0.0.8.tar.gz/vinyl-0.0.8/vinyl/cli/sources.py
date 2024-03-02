import os

import typer
from rich.console import Console
from rich.table import Table
from tqdm import tqdm

from vinyl.lib.connect import (
    DatabaseFileConnector,
    SourceInfo,
    _DatabaseConnector,
    _FileConnector,
    _TableConnector,
)
from vinyl.lib.definitions import _load_project_defs
from vinyl.lib.project import Project, _load_project_module
from vinyl.lib.source import _get_twin_relative_path
from vinyl.lib.utils.ast import (
    _find_classes_and_attributes,
    _get_imports_from_file_regex,
)
from vinyl.lib.utils.files import _create_dirs_with_init_py
from vinyl.lib.utils.functions import _with_modified_env
from vinyl.lib.utils.text import _make_python_identifier

_console = Console()


_sources_cli = typer.Typer(pretty_exceptions_show_locals=False)


@_sources_cli.command("list")
def _list_sources(tables: bool = False):
    """Caches sources to a local directory (default: .turntable/sources)"""
    defs = _load_project_defs()
    project = Project(resources=defs.resources, models=defs.models)

    table = Table("Name", "Resource", "Location", title="Sources")
    for source in project._get_source_objects():
        if source._parent_resource is None:
            raise ValueError("Source must have a parent resource.")
        table.add_row(
            f"[bold]{source._name}[bold]",
            f"[grey70]{source._parent_resource.def_.__name__}[grey70]",
            f"[grey70]{source._location}[grey70]",
        )
    _console.print(table)


def _table_to_python_class(table_name) -> str:
    return "".join([word.capitalize() for word in table_name.split("_")])


def _source_to_class_string(
    source: SourceInfo,
    saved_attributes: dict[str, str],
    generate_twin: bool = False,
    root_path: str | None = None,
    sample_size: int = 1000,
) -> str:
    if not root_path:
        module_file = _load_project_module().__file__
        if module_file is None:
            raise ValueError("Unable to find the module path for the current project")
        os.path.dirname(module_file)

    class_name = _table_to_python_class(source._name)
    class_body = f'    _table = "{source._name}"\n'
    pr = source._parent_resource

    if pr is None:
        raise ValueError("Source must have a parent resource.")

    if isinstance(pr.connector, _TableConnector):
        tbl = pr.connector._get_table(source._location)
        class_body += f'    _unique_name = "{pr.name}.{class_name}"\n'

    elif isinstance(pr.connector, _DatabaseConnector):
        # source is a database
        database, schema = source._location.split(".")
        class_body += (
            f'    _unique_name = "{pr.name}.{source._location}.{class_name}"\n'
        )
        class_body += f'    _schema = "{schema}"\n'
        class_body += f'    _database = "{database}"\n'

        database, schema = source._location.split(".")
        tbl = pr.connector._get_table(database, schema, source._name)
        class_body += f'    _twin_path = "{_get_twin_relative_path(pr.name, database, schema)}"\n\n'
        # need row count if using local files (since sampling is done live from the file)

    else:
        raise NotImplementedError(
            f"Connector type {type(pr.connector)} is not yet supported"
        )

    # need row count if using local files (since sampling is done live from the file)
    if isinstance(pr.connector, _FileConnector):
        if isinstance(pr.connector, DatabaseFileConnector):
            # in this case, location is not the real path, but the database and schema, but we can use the path from the connector
            path = os.path.relpath(pr.connector._path, root_path)
        else:
            path = os.path.relpath(source._location, root_path)
        class_body += f'    _path = "{path}"\n'
        if not pr.connector._remote:
            # in this case, we will not be caching the table, so we need the row_count
            class_body += f"    _row_count = {tbl.count().execute()}\n\n"

    if source._schema is None:
        raise ValueError(f"Schema for {source._name} is not available")

    for col_name, col_type in source._schema.items():
        base = f"    {col_name.lower().replace(' ', '_')}: t.{col_type.__repr__()}"
        if col_name in saved_attributes:
            base += f" = {saved_attributes[col_name]}"
        class_body += f"{base}\n"

    out = f"""class {class_name}:
{class_body}
"""
    return out


def _get_save_dir(sources_path: str, source: SourceInfo) -> str:
    if source._parent_resource is None:
        raise ValueError("Source must have a parent resource.")
    if isinstance(source._parent_resource.connector, _TableConnector):
        # source is a file
        return os.path.join(sources_path, source._parent_resource.name)
    if isinstance(source._parent_resource.connector, _DatabaseConnector):
        # source is a database
        identifers = [
            _make_python_identifier(str_) for str_ in source._location.split(".")
        ]
        return os.path.join(sources_path, source._parent_resource.name, *identifers)
    raise NotImplementedError(
        f"Connector type {type(source._parent_resource.connector)} is not yet supported"
    )


@_sources_cli.command("generate")
def _generate_sources(
    twin: bool = typer.Option(
        False, "--generate_twin", "-t", help="exported name of the model"
    ),
    resources: list[str] = typer.Option(
        [], "--resource", "-r", help="resource names to select"
    ),
):
    """Generates schema files for sources"""

    @_with_modified_env("NO_MODELS_VINYL", "True")
    def run_fn():
        defs = _load_project_defs()
        if len(resources) == 0:
            project = Project(resources=defs.resources)
        else:
            project = Project(
                resources=[r for r in defs.resources if r.__name__ in resources]
            )
        root_path = os.path.dirname(_load_project_module().__file__)
        sources = project._get_source_objects(with_schema=True)

        sources_path = os.path.join(root_path, "sources")
        _create_dirs_with_init_py(sources_path)

        for source in sources:
            save_dir = _get_save_dir(sources_path, source)
            _create_dirs_with_init_py(save_dir)
            file_path = os.path.join(save_dir, f"{source._name}.py")
            try:
                saved_attributes = _find_classes_and_attributes(file_path)
            except (IndexError, FileNotFoundError):
                saved_attributes = {}
            saved_imports = (
                _get_imports_from_file_regex(file_path)
                if saved_attributes != {}
                else None
            )
            with open(os.path.join(save_dir, f"{source._name}.py"), "w+") as f:
                if saved_imports:
                    f.write(saved_imports)
                else:
                    f.write("# type: ignore\n")  # prevents pylance errors tied to Ibis
                    f.write("from vinyl import Field, source # noqa F401\n")
                    f.write("from vinyl import types as t # noqa F401\n\n")
                    f.write(
                        f"from {source._parent_resource.def_.__module__} import {source._parent_resource.def_.__name__} # noqa F401 \n\n\n"
                    )
                f.write(f"@source(resource={source._parent_resource.name})\n")
                f.write(
                    _source_to_class_string(
                        source, saved_attributes, root_path=root_path
                    )
                )

        if twin:
            msg = "generating twins... " if len(sources) > 1 else "generating twin... "
            for source in tqdm(
                sources,
                msg,
                unit="source",
            ):
                pr = source._parent_resource
                if isinstance(pr.connector, _DatabaseConnector):
                    database, schema = source._location.split(".")
                    pr.connector._generate_twin(
                        os.path.join(root_path, _get_twin_relative_path(pr.name)),
                        database,
                        schema,
                        source.name,
                    )
                elif isinstance(pr.connector, _TableConnector):
                    # doesn't actually generate a file, just returns the path
                    pr.connector._generate_twin(source.location)

        print(f"Generated {len(sources)} sources at {sources_path}")

    run_fn()
