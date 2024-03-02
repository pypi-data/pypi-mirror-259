from typing import Any

import ibis
from ibis.expr.types import BooleanValue, Value

from vinyl.lib.column import _demote_args
from vinyl.lib.utils.functions import _validate


def case(
    pairs: list[tuple[BooleanValue, Value]], default: Value | None = None
) -> Value:
    """
    Returns the first value for which the corresponding condition is true. If no conditions are true, return the default.

    Conditions should be specified as a list of tuples, where the first element of each tuple is a boolean expression and the second element is the value to return if the condition is true.
    """
    if len(pairs) == 0:
        raise ValueError("At least one pair must be provided")
    elif len(pairs) == 1:
        return ibis.ifelse(pairs[0][0], pairs[0][1], default)

    out = ibis.case()
    for pair in pairs:
        out = out.when(pair[0], pair[1])
    out = out.else_(default)
    return out.end()


def if_else(condition: BooleanValue, true_value: Value, false_value: Value) -> Value:
    """
    Constructs a conditional expression. If the condition is true, return the true_value; otherwise, return the false_value.

    Can be chained together by making the true_value or false_value another if_else expression.
    """
    return ibis.ifelse(condition, true_value, false_value)


def coalesce(*args: Value) -> Value:
    """
    Return the first non-null value in the expression list.
    """
    return ibis.coalesce(*args)


def least(*args: Any) -> Value:
    """
    Return the smallest value among the supplied arguments.
    """
    return ibis.least(*args)


def greatest(*args: Any) -> Value:
    """
    Return the largest value among the supplied arguments.
    """
    return ibis.greatest(*args)


# Adjust the function arguments to work with VinylColumn syntax and add validation
case = _validate(_demote_args(case))
if_else = _validate(_demote_args(if_else))
coalesce = _validate(_demote_args(coalesce))
least = _validate(_demote_args(least))
greatest = _validate(_demote_args(greatest))
