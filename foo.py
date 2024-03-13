# foo.py
from __future__ import annotations
from typing import Protocol, TypeVar

from . import mod1
from . import mod2

DataFrame = TypeVar("DataFrame", mod1.DataFrame, mod2.DataFrame)


class Namespace(Protocol):
    DataFrame: type[mod1.DataFrame] | type[mod2.DataFrame]


def get_namespace(thing: mod1.DataFrame | mod2.DataFrame) -> Namespace:
    if isinstance(thing, mod1.DataFrame):
        # Mypy complains that mod*.DataFrame is not a union
        return mod1  # type: ignore
    elif isinstance(thing, mod2.DataFrame):
        return mod2  # type: ignore
    raise ValueError


def things_that_work(df: mod1.DataFrame | mod2.DataFrame):
    _a: str = df.foo_and_bar_same_type
    _b: int | str = df.foo_and_bar_different_type
    df.different_arity("asdf")
    df.different_kw_only("asdf", y="asdf")

    ns = get_namespace(df)
    _c: mod1.DataFrame | mod2.DataFrame = ns.DataFrame()
    

def things_that_produce_errors(df: mod1.DataFrame | mod2.DataFrame):
    # Item "Bar" of "Union[Foo, Bar]" has no attribute "only_foo"  [union-attr] (python-mypy)
    df.only_foo

    # Incompatible types in assignment (expression has type "Union[int, str]", variable has type "int")  [assignment] (python-mypy)
    _a: int = df.foo_and_bar_different_type

    # Too many arguments for "different_arity"  [call-arg] (python-mypy)
    df.different_arity("asdf", "asdf")

    # Too many positional arguments for "different_kw_only"  [misc] (python-mypy)
    df.different_kw_only("asdf", "asdf")

    ns = get_namespace(df)
    # Incompatible types in assignment (expression has type "Union[tests.mod1.DataFrame, tests.mod2.DataFrame]",
    # variable has type "tests.mod1.DataFrame")  [assignment] (python-mypy)
    _c: mod1.DataFrame = ns.DataFrame()


def compute(df: DataFrame) -> DataFrame:
    return mod1.DataFrame()
