import ibis
from ibis.expr.types import Column, IntegerColumn, IntegerValue

from vinyl.lib.column import _demote_args
from vinyl.lib.utils.functions import _validate


def row_number() -> IntegerColumn:
    """
    Returns the current row number.

    This function is normalized across backends to start from 0.
    """
    return ibis.row_number()


def rank(dense: bool = False) -> IntegerColumn:
    """
    Compute position of first element within each equal-value group in sorted order.

    If `dense` don't skip records after ties. See [here](https://learnsql.com/cookbook/whats-the-difference-between-rank-and-dense_rank-in-sql/) for a good primer on the difference.

    """
    if dense:
        return ibis.dense_rank()
    return ibis.rank()


def percent_rank() -> Column:
    """
    Compute the relative rank of a value within a group of values.
    """
    return ibis.percent_rank()


def ntile(n: int | IntegerValue) -> IntegerColumn:
    """
    Divide the rows into `n` buckets, assigning a bucket number to each row.
    """
    return ibis.ntile(n)


# Adjust the function arguments to work with VinylColumn syntax and add validation
row_number = _validate(_demote_args(row_number))
rank = _validate(_demote_args(rank))
percent_rank = _validate(_demote_args(percent_rank))
ntile = _validate(_demote_args(ntile))
