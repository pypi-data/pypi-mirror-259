import itertools
from pathlib import Path

import toml


def _get_root() -> Path | None:
    # Create a Path object for the start directory
    path = Path().resolve()

    # Traverse up through the parent directories
    for parent in itertools.chain([path], path.parents):
        pyproject_toml = parent / "pyproject.toml"
        if pyproject_toml.exists():
            return pyproject_toml.parent.absolute()

    return None


class PyProjectSettings:
    _toml: dict

    def __init__(self, path: Path | None = None):
        if path is None:
            path = _get_root()
            if path is None:
                raise FileNotFoundError("pyproject.toml not found")
        with open(path / "pyproject.toml") as f:
            self._toml = toml.load(f)

    def _get_setting(self, key: str) -> str | None:
        return self._toml["tool"]["vinyl"].get(key, None)
