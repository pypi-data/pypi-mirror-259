from functools import reduce, wraps
from typing import Literal

import ibis

from vinyl.lib.column import _demote_args
from vinyl.lib.set_methods import (
    _auto_join_helper,
    _convert_auto_join_to_ibis_join,
    base_join_type,
)
from vinyl.lib.table import VinylTable, _base_ensure_output
from vinyl.lib.table_methods import _difference_two, _intersect_two, _union_two
from vinyl.lib.utils.functions import _validate


def _ensure_output_left(func):
    @wraps(func)
    def wrapper(left: VinylTable, *args, **kwargs) -> VinylTable:
        return _base_ensure_output(func, left, *args, **kwargs)

    return wrapper


def _ensure_output_first(func):
    @wraps(func)
    def wrapper(first: VinylTable, *args, **kwargs) -> VinylTable:
        return _base_ensure_output(func, first, *args, **kwargs)

    return wrapper


@_ensure_output_left
def join(
    left: VinylTable,
    right: VinylTable,  # will be a VinylTable, but pydantic can't validate
    *,
    auto: bool = True,
    auto_allow_cross_join: bool = False,
    on: base_join_type | list[base_join_type] = [],
    how: Literal[
        "inner",
        "left",
        "outer",
        "right",
        "semi",
        "anti",
        "any_inner",
        "any_left",
        "left_semi",
    ] = "inner",
    lname: str = "",
    rname: str = "{name}_right",
) -> VinylTable:
    left = left.copy(mutable=False)
    right = right.copy(mutable=False)

    if auto and on == []:
        nodes, edges = _auto_join_helper(
            [left, right], allow_cross_join=auto_allow_cross_join
        )
        first = nodes[0]
        other_nodes = nodes[1:]

        # need to ensure output to pass on all nodes into connection dicts, may be more than just left and right. We do this by making all nodes a top-level arg and using the features of ensure_output
        @_ensure_output_first
        def auto_join_iteration(first, *other_nodes, edges):
            nodes = [first, *other_nodes]
            return _convert_auto_join_to_ibis_join(nodes, edges)

        return auto_join_iteration(first, *other_nodes, edges=edges)

    base_join = ibis.join(
        left=left.tbl,
        right=right.tbl,
        predicates=on,
        how=how,
        lname=lname,
        rname=rname,
    )
    return base_join


def union(first: VinylTable, *rest: VinylTable, distinct: bool = False) -> VinylTable:
    """
    Compute the set union of multiple table expressions.

    Unlike the SQL UNION operator, this function allows for the union of tables with different schemas. If a column is present in one table but not in another, the column will be added to the other table with NULL values.

    If `distinct` is True, the result will contain only distinct rows. If `distinct` is False, the result will contain all rows from all tables, including duplicates.
    """
    if len(rest) == 0:
        return first

    return reduce(lambda x, y: _union_two(x.tbl, y.tbl, distinct), rest, first)


def difference(
    first: VinylTable, *rest: VinylTable, distinct: bool = False
) -> VinylTable:
    """
    Compute the set difference of multiple table expressions.

    Unlike the SQL EXCEPT operator, this function allows for the difference of tables with different schemas. If a column is present in one table but not in another, the column will be added to the other table with NULL values.

    If `distinct` is True, the result will contain only distinct rows. If `distinct` is False, the result will contain all rows from the first table, including duplicates.
    """
    if len(rest) == 0:
        return first

    return reduce(lambda x, y: _difference_two(x.tbl, y.tbl, distinct), rest, first)


def intersect(
    first: VinylTable, *rest: VinylTable, distinct: bool = True
) -> VinylTable:
    """
    Compute the set intersection of multiple table expressions.

    Unlike the SQL INTERSECT operator, this function allows for the intersection of tables with different schemas. If a column is present in one table but not in another, the column will be added to the other table with NULL values.

    If `distinct` is True, the result will contain only distinct rows. If `distinct` is False, the result will contain all rows that are present in all tables, including duplicates.
    """
    if len(rest) == 0:
        return first

    return reduce(lambda x, y: _intersect_two(x.tbl, y.tbl, distinct), rest, first)


# Add pydantic validations and arg demotion. Need to demote_args outside of the function to ensure validation (and function) works correctly.
join = _demote_args(_validate(join))  # type: ignore[method-assign]
union = _demote_args(_validate(union))  # type: ignore[method-assign]
difference = _demote_args(_validate(difference))  # type: ignore[method-assign]
intersect = _demote_args(_validate(intersect))  # type: ignore[method-assign]
