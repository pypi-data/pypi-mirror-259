from __future__ import annotations

import re
from typing import Any

import ibis.expr.operations as ops
import ibis.expr.types as ir
import networkx as nx
import rustworkx as rx
from ibis.expr.datatypes import DataType

from vinyl.lib.column import _demote_arg
from vinyl.lib.utils.graph import _rustworkx_to_networkx


class Field:
    _relations: rx.PyDiGraph = rx.PyDiGraph()
    _relations_node_dict: dict[str, int] = {}
    _source_class_dict: dict[ir.Table, Any] = {}
    _source_adj_tbl_dict: dict[str, Any] = {}  # will be VinylTable
    name: str | None
    type: DataType | None
    description: str | None
    unique: bool
    primary_key: bool
    foreign_key: Field | None
    pii: bool
    _parent_name: str | None
    _parent_ibis_table: object | None
    _parent_vinyl_table: object | None

    def __init__(
        self,
        name: str | None = None,
        type: DataType | None = None,
        description: str | None = None,
        primary_key: bool = False,
        foreign_key: Field | None = None,
        unique: bool = False,
        pii: bool = False,
        parent_name: str | None = None,
        parent_ibis_table: ops.UnboundTable | None = None,
        parent_vinyl_table: Any | None = None,
    ):
        self._parent_name = parent_name
        self._parent_ibis_table = parent_ibis_table
        self._parent_vinyl_table = parent_vinyl_table
        self.name = name
        self.type = type
        self.description = description
        self.primary_key = primary_key
        self.unique = unique
        self.foreign_key = _demote_arg(
            foreign_key
        )  # necessary because foreign key may be VinylColumn, not Ibis Column
        self.pii = pii

    def _update_source_class(self):
        self._source_class_dict[self._parent_vinyl_table] = (
            self._parent_vinyl_table._source_class
            if hasattr(self._parent_vinyl_table, "_source_class")
            else None
        )

    def _store_source_adj_tbl(
        self, vinyl_tbl: Any
    ):  # will be VinylTable, but can't state due to circular import
        hash_ = str(hash(self._parent_ibis_table))
        if hash_ not in self._source_adj_tbl_dict:
            self._source_adj_tbl_dict[hash_] = vinyl_tbl

    def _store_relations(self):
        self_parent_table_vinyl = self._source_adj_tbl_dict[
            str(hash(self._parent_ibis_table))
        ]
        self._add_node(self_parent_table_vinyl)
        if self.foreign_key is not None:
            foreign_key_op = self.foreign_key.op()
            # note for below, foriegn key class has been imported, so self.foreign_key is an ibis expression at this point
            foreign_key_parent_table_ibis = foreign_key_op.find(ops.UnboundTable)[
                0
            ].to_expr()
            foreign_key_name = foreign_key_op.args[-1]
            foreign_key_parent_table_vinyl = self._source_adj_tbl_dict[
                str(hash(foreign_key_parent_table_ibis))
            ]

            self._add_edge(
                foreign_key_parent_table_vinyl,
                self_parent_table_vinyl,
                (foreign_key_name, self.name),
            )

            if self.unique:
                # relationship is bidirectional, so we need to add the edge in both directions
                self._add_edge(
                    self_parent_table_vinyl,
                    foreign_key_parent_table_vinyl,
                    (self.name, foreign_key_name),
                )

    def _add_node(self, node: ir.Expr):
        hash_ = str(hash(node))
        if hash_ not in self._relations_node_dict:
            self._relations_node_dict[hash_] = self._relations.add_node(node)

    def _add_edge(
        self,
        node1: ir.Expr,
        node2: ir.Expr,
        data: Any,
    ):
        for node in [node1, node2]:
            self._add_node(node)

        self._relations.add_edge(
            self._relations_node_dict[str(hash(node1))],
            self._relations_node_dict[str(hash(node2))],
            data,
        )

    def _asdict(self):
        out = {}
        for k, v in self.__dict__.items():
            if v is not None and k != "_relations":
                out[k] = v

        return out

    def _update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def _export_relations_to_networkx(
        cls, shorten_name: bool = True, filter: list[str] | None = None
    ) -> nx.Graph | nx.DiGraph | nx.MultiGraph | nx.MultiDiGraph:
        G = _rustworkx_to_networkx(cls._relations)
        # make sure node object is passed as data rather than name to prevent issues with renderer
        nx.set_node_attributes(G, {node: node for node in G.nodes()}, "node")

        if shorten_name or filter:
            nx.relabel_nodes(
                G, {node: node.get_name() for node in G.nodes()}, copy=False
            )

        if not filter:
            return G
        else:
            all_nodes = list(G.nodes())
            nodes_in_subgraph: set[str] = set()
            for fil in filter:
                regex = re.compile(fil)
                nodes_to_add = set(node for node in all_nodes if regex.search(node))
                nodes_in_subgraph = nodes_in_subgraph.union(nodes_to_add)

            return G.subgraph(nodes_in_subgraph)
