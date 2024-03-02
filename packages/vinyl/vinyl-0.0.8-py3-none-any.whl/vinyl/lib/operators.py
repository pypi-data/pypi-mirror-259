from __future__ import annotations

from typing import Any, Callable


class Infix(object):
    function: Callable[..., Any]

    def __init__(self, function):
        self.function = function

    def __rmod__(self, other) -> Infix:
        return Infix(lambda x: self.function(other, x))

    def __mod__(self, other) -> Any:
        return self.function(other)


like: Infix = Infix(lambda x, y: x.like(y))
ilike: Infix = Infix(lambda x, y: x.ilike(y))
isin: Infix = Infix(lambda x, y: x.isin(y))
notin: Infix = Infix(lambda x, y: x.notin(y))
is_: Infix = Infix(lambda x, y: x.isnull() if y is None else x == y)
isnt: Infix = Infix(lambda x, y: x.notnull() if y is None else x != y)
