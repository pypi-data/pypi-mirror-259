import os
import shutil

import typer

from .preview import _preview_cli
from .project import _project_cli
from .sources import _sources_cli
from importlib.metadata import version as get_version

_app: typer.Typer = typer.Typer(pretty_exceptions_show_locals=False)
_app.add_typer(_preview_cli, name="preview")
_app.add_typer(_sources_cli, name="sources")
_app.add_typer(_project_cli, name="project")


@_app.callback(invoke_without_command=True)
def _main(
    ctx: typer.Context,
    version: bool = typer.Option(
        None,
        "--version",
    ),
):
    if version:
        typer.echo(f"Vinyl version: {get_version('vinyl')}")
        return 0

    if ctx.invoked_subcommand is not None:
        return 0

    typer.echo(ctx.get_help())
    return 0


@_app.command("init")
def _init_project(project_name: str):
    """Initialize a new Vinyl project and it's file strucutre"""
    normalized_project_name = project_name.lower().replace(" ", "_")
    scaffolding_path = os.path.join(os.path.dirname(__file__), "_project_scaffolding")
    project_path = os.path.join(os.getcwd(), normalized_project_name)
    if os.path.exists(project_path):
        raise ValueError(f"Directory {project_path} already exists")

    # copy the scaffolding to the new project path
    shutil.copytree(scaffolding_path, project_path)
    # rename the project folder
    os.rename(
        os.path.join(project_path, "__project_name__"),
        os.path.join(project_path, normalized_project_name),
    )

    # templatize project assets
    project_assets = [
        "README.md",
        "pyproject.toml",
    ]
    asset_paths = [os.path.join(project_path, asset) for asset in project_assets]
    for path in asset_paths:
        with open(path, "r") as f:
            content = f.read()
        content = content.replace("{{PROJECT_NAME}}", normalized_project_name)
        with open(path, "w") as f:
            f.write(content)
    # change imports in the models.py file
    models_path = os.path.join(
        project_path, normalized_project_name, "models", "models.py"
    )
    with open(models_path, "r") as f:
        content = f.read()
        content_to_write = content.replace("__project_name__", normalized_project_name)
    with open(models_path, "w") as f:
        f.write(content_to_write)

    typer.echo(f"Created project at {project_path}")


if __name__ == "__main__":
    _app()
