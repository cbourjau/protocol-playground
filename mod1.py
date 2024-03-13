# mod1.py
class DataFrame:
    only_foo: int
    foo_and_bar_same_type: str
    foo_and_bar_different_type: int

    def different_arity(self, x):
        ...

    def different_kw_only(self, x, *, y):
        ...
