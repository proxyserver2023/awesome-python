# Concepts

## Metaclass

### Why do we need metaclass?

By default in `python3` a class is inherited from basetype `type`. At the time some default initialization takes place like `__call__()` and then `__new__()`, `__init__()`. If we want to override it we need to extend the base type `type` and create another class that would be our metaclass. and from then we will use that metaclass. Because we dont want to temper with the built-in features.

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases,dct)
        x.attr = 100
        return x

class Foo(metaclass=Meta):
    pass

# Foo.attr - 100
```

## Importing Modules and Packages

- **testcase - 1**: we can call a script from wherever, as long as the imported modules resides relative to the **script directory**.

```shell
$ cd
$ mkdir -p new1/new2/new3
$ touch main.py new1/new2/new3/{main, mod}.py
```

In `mod.py`

```python
s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    def __str__(self):
        return 'Class-Foo'
```

In `main.py`

```python
import mod

print(mod.s)

print(mod.a)

mod.foo('alamin')

f = mod.Foo()
print(f)
```

Now if I call it from anywhere assuming `main.py` and `mod.py` resides at same place. It will work.

- **testcase - 2A**: we can call a module, if it resides into a sub-directory and it doesn't have to be a package.

```
.
| - main.py
| - a
  | - mod.py
```

```shell
$ python3 ./main.py
```

- **testcase - 2B**: we can call a module with a nested package.

```
.
| - main.py
| - a
  | - __init__.py
  | - mod.py
```

```shell
$ python3 ./main.py
```

- **testcase - 3**: Calling a module of another package.

```
.
├── a
│   ├── __init__.py
│   ├── mod.py
├── b
│   ├── main.py

```

```shell
$ python3 ./b/main.py

Traceback (most recent call last):
  File "b/main.py", line 1, in <module>
    from a import mod
ModuleNotFoundError: No module named 'a'
Error in sys.excepthook:
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/apport_python_hook.py", line 63, in apport_excepthook
    from apport.fileutils import likely_packaged, get_recent_crashes
  File "/usr/lib/python3/dist-packages/apport/__init__.py", line 5, in <module>
    from apport.report import Report
  File "/usr/lib/python3/dist-packages/apport/report.py", line 30, in <module>
    import apport.fileutils
  File "/usr/lib/python3/dist-packages/apport/fileutils.py", line 23, in <module>
    from apport.packaging_impl import impl as packaging
  File "/usr/lib/python3/dist-packages/apport/packaging_impl.py", line 24, in <module>
    import apt
  File "/usr/lib/python3/dist-packages/apt/__init__.py", line 23, in <module>
    import apt_pkg
ModuleNotFoundError: No module named 'apt_pkg'

Original exception was:
Traceback (most recent call last):
  File "b/main.py", line 1, in <module>
    from a import mod
ModuleNotFoundError: No module named 'a'

```

To access `a/mod.py` inside `b/main.py` we need to include `a` package into [Module Search Path](#module-search-path)

### Module Search Path

- The directory from which the input script was run (the script resides) or the current directory if the interpreter is being run interactively
- The list of directories contained in the `PYTHONPATH` environment variable, if it is set. (The format for `PYTHONPATH` is OS-dependent but should mimic the `PATH` environment variable.)
- An installation-dependent list of directories configured at the time Python is installed

## Symbol Table

Symbol Table holds the variable name, address and types. Programming Language like python support nested blocks. Symbol Tables are created Blockwise hierarchically.

![Symbol-Table-TutorialsPoint](https://www.tutorialspoint.com/compiler_design/images/symbol_table.jpg)

### Variables in Python are referenced to objects

Python doesn't really have variables in the sense C has. Rather, Python has symbolic names bound to objects:

```python
aa = [1, 2, 3]

id(aa) # 140240689021384
bb = aa

id(bb) # 140240689021384
aa[0] = 666

print(aa) # [666, 2, 3]
print(bb) # [666, 2, 3]
```
