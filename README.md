# Playground to evaluate mypy's capabilities


```
micromamba env create -f environment.yml
micromamba activate protocol-playground
mypy foo.py
```

yields:
```
foo.py:36: error: Item "protocol.mod2.DataFrame" of "protocol.mod1.DataFrame | protocol.mod2.DataFrame" has no attribute "only_foo"  [union-attr]
foo.py:39: error: Incompatible types in assignment (expression has type "int | str", variable has type "int")  [assignment]
foo.py:42: error: Too many arguments for "different_arity"  [call-arg]
foo.py:45: error: Too many positional arguments for "different_kw_only"  [misc]
foo.py:50: error: Incompatible types in assignment (expression has type "protocol.mod1.DataFrame | protocol.mod2.DataFrame", variable has type "protocol.mod1.DataFrame")  [assignment]
foo.py:54: error: Incompatible return value type (got "protocol.mod1.DataFrame", expected "protocol.mod2.DataFrame")  [return-value]
Found 6 errors in 1 file (checked 1 source file)
```
