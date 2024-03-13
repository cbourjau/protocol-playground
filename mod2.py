# mod2.py
class DataFrame:
    bar: int
    foo_and_bar_same_type: str
    foo_and_bar_different_type: str

    def different_arity(self, x, y=None):
        ...

    def different_kw_only(self, x, y):
        ...
