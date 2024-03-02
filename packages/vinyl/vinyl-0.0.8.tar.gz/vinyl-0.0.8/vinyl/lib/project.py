import dataclasses
import importlib
import os
import sys
from types import ModuleType
from typing import Any, Callable

import ibis.expr.types as ir
import toml

from vinyl.lib.connect import SourceInfo, _ResourceConnector
from vinyl.lib.metric import MetricStore
from vinyl.lib.table import VinylTable
from vinyl.lib.utils.pkg import _find_nearest_pyproject_toml_directory


def _get_project_module_name() -> str:
    root_path = _find_nearest_pyproject_toml_directory()

    with open(root_path, "r") as file:
        data = toml.load(file)

    return data["tool"]["vinyl"]["module_name"]


def _load_project_module() -> ModuleType:
    # Backup the original sys.modules
    try:
        module_name = _get_project_module_name()
    except KeyError:
        raise ValueError("Can't find a project pyproject.toml file.")

    sys.path.append(os.getcwd())
    imported_module = importlib.import_module(module_name)
    return imported_module


@dataclasses.dataclass
class Resource:
    name: str
    connector: _ResourceConnector
    def_: Any


class Project:
    resources: list[Resource]
    sources: list[ir.Table]
    models: list[Callable[..., Any]]
    metrics: list[Callable[..., Any]]

    def __init__(
        self,
        resources: list[Callable[..., Any]],
        sources: list[ir.Table] | None = None,
        models: list[Callable[..., Any]] | None = None,
        metrics: list[Callable[..., Any]] | None = None,
    ):
        self.resources = [
            Resource(
                name=resource_def.__name__,
                def_=resource_def,
                connector=resource_def(),
            )
            for resource_def in resources
        ]
        if sources is not None:
            self.sources = sources
        if models is not None:
            self.models = models
        if metrics is not None:
            self.metrics = metrics

    def _get_source_objects(self, with_schema=False) -> list[SourceInfo]:
        sources = []
        for resource in self.resources:
            try:
                resource_sources = resource.connector._list_sources(with_schema)
                for source in resource_sources:
                    source._parent_resource = resource
                    sources.append(source)
            except Exception as e:
                print(f"Error loading sources from {resource.name}: {e}")
                continue
        return sources

    def _get_resource(self, resource_name: str) -> Resource:
        resources = [
            resource for resource in self.resources if resource.name == resource_name
        ]

        if len(resources) == 0:
            raise ValueError(f"Resource {resource_name} not found")

        resource = resources[0]

        return resource

    def _get_source(self, source_id: str):
        sources = [source for source in self.sources if source.__name__ == source_id]

        if len(sources) == 0:
            raise ValueError(f"Source {source_id} not found")

        source = sources[0]

        return source

    def _get_model(self, model_id: str) -> VinylTable:
        if self.models is None:
            raise ValueError("No models found")
        models = [model for model in self.models if model.__name__ == model_id]

        if len(models) == 0:
            raise ValueError(f"Model {model_id} not found")

        model = models[0]

        return model()

    def _get_metric_store(self, metric_id: str) -> MetricStore:
        metrics = [metric for metric in self.metrics if metric.__name__ == metric_id]
        if len(metrics) == 0:
            raise ValueError(f"Metric {metric_id} not found")

        metric = metrics[0]

        return metric()
