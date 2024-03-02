import dataclasses

import typer
from textual.app import ComposeResult
from textual.widgets import DataTable, Footer

from vinyl import Field
from vinyl.lib.constants import PreviewHelper
from vinyl.lib.definitions import _load_project_defs
from vinyl.lib.erd import _create_erd_app
from vinyl.lib.project import Project
from vinyl.lib.query_engine import QueryEngine
from vinyl.lib.utils.graphics import TurntableTextualApp

_preview_cli: typer.Typer = typer.Typer(pretty_exceptions_show_locals=False)


class PreviewTable(TurntableTextualApp):
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        super().__init__()

    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*self._columns)
        table.add_rows(self._rows)


@_preview_cli.command("model")
def _preview_model(
    name: str = typer.Option(
        False, "--name", "-m", help="exported name of the model or source"
    ),
    twin: bool = typer.Option(False, "--twin", "-t", help="use twin data"),
):
    """Preview a model"""
    if twin:
        PreviewHelper._preview = "twin"

    defs = _load_project_defs()
    project = Project(**dataclasses.asdict(defs))
    query_engine = QueryEngine(project)
    result = query_engine._model(name, limit=1000)
    app = PreviewTable(columns=tuple(result.columns()), rows=result.numpy_rows())
    app.run()


@_preview_cli.command("metric")
def _preview_metric(
    name: str = typer.Option(..., help="exported name of the metric column"),
    grain: str = typer.Option(
        ..., help="grain to bucket the metric by (ex: months=3, year=1)"
    ),
    dims: list[str] = typer.Option(
        None, "--dims", help="comma separated list of dimensions to include"
    ),
    cols: list[str] = typer.Option(
        None, "--cols", help="comma separated list of columns to include"
    ),
):
    """Preview a model"""
    defs = _load_project_defs()
    project = Project(**dataclasses.asdict(defs))
    query_engine = QueryEngine(project)
    result = query_engine._metric(name, grain, 1000)

    app = PreviewTable(
        columns=result.columns(),
        rows=result.numpy_rows(),
    )
    app.run()


@_preview_cli.command("erd")
def _erd(
    names: list[str] = typer.Option(
        [], "--name", "-m", help="exported name(s) of the model or source"
    ),
):
    """Generate an ERD"""
    _load_project_defs()
    G = Field._export_relations_to_networkx(
        shorten_name=True, filter=None if len(names) == 0 else names
    )
    _create_erd_app(G).run()
