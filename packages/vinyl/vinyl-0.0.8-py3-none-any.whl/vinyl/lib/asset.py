import functools
import inspect
from functools import wraps
from typing import Any, Callable
from vinyl.lib.enums import AssetType

from vinyl.lib.metric import MetricStore
from vinyl.lib.table import VinylTable
from vinyl.lib.utils.functions import _validate

@_validate
def _base(
    deps: object | Callable[..., Any] | list[object | Callable[..., Any]],
    asset_type: AssetType | None = None,
    publish: bool = False,
    tags: str | list[str] | None = None,
):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            if not isinstance(deps, list):
                deps_adj = [deps]
            else:
                deps_adj = deps
            # Map the positional arguments to the new names
            params = [
                param.name for param in inspect.signature(func).parameters.values()
            ]
            if len(params) != len(deps_adj):
                raise Exception("Wrong number of arguments")

            new_kwargs = {}
            # do dependency injection for each param of the function

            for i, param in enumerate(params):
                # TODO: this is a hack to avoid mutable sources and models from being impacted downstream
                # we should eventually clean this up as it's not a sustainable solution
                dep_it = deps_adj[i]()
                if isinstance(dep_it, (VinylTable, MetricStore)):
                    par = dep_it.copy()

                else:
                    raise ValueError(
                        f"Dependencies must be VinylTable or MetricStore, not {type(dep_it)}"
                    )

                par._mutable = True
                new_kwargs[param] = par

            return func(**new_kwargs)

        setattr(wrapper, f"_is_vinyl_{asset_type.value}", True)

        return wrapper

    return decorator


@_validate
def model(
    deps: object | Callable[..., Any] | list[object | Callable[..., Any]],
    publish: bool = False,
    tags: str | list[str] | None = None,
):
    return _base(deps, AssetType.MODEL, publish, tags)


@_validate
def metric(
    deps: object | Callable[..., Any] | list[object | Callable[..., Any]],
    publish: bool = False,
    tags: str | list[str] | None = None,
):
    return _base(deps, AssetType.METRIC, publish, tags)


def resource(func: Callable[..., Any]):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        return func(*args, **kwargs)

    decorated_function._is_vinyl_resource = True  # type: ignore
    return decorated_function
