# Awesome Python Examples

Codebase for excellent python project examples.

## Table of Contents

- [Getting Started](#getting-started)
- [Concepts](#concepts)
  - [Metaclass](#metaclass)
  - [Importing Modules and Packages](#importing-modules-and-packages)
  - [Symbol Table](#symbol-table)
    - [Variables in Python are referenced to objects](#variables-in-python-are-referenced-to-objects)
- [Best Practices](#best-practices)
- [References](#references)
  - [Reserved Classes of Identifiers](#Reserved-Classes-of-Identifiers)
  - [is vs ==](#is-vs-equal)
  - [site packages vs dist packages](#site-packages-vs-dist-packages)
- [Resources](#resources)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- python3
- pip3
- virtualenvwrapper

Install `python3`

```bash
sudo apt-get install -y python3
```

Install `pip3`

```bash
sudo apt-get install -y python3-pip
sudo pip3 install --upgrade pip
pip3 --version
```

Install `virtualenvwrapper`

```bash
sudo pip3 install virtualenvwrapper
```

On your `.zshrc` or `.bashrc`

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/projects
source /usr/local/bin/virtualenvwrapper.sh

# change `which python2.*` to pyhton3 if need
# nano /usr/local/bin/virtualenvwrapper.sh
```

```bash
source ~/.bashrc
#or
source ~/.zshrc
```

### Installing

Create a virtualenv

```bash
mkvirtualenv awesome-python
workon awesome-python
```

Clone the Repo

```bash
git clone https://github.com/AlaminMahamud/awesome-python
cd awesome-python
```

Install the requirements

```bash
pip install -r requirements.txt
```

## Concepts

### Metaclass

#### Why do we need metaclass?

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

### Importing Modules and Packages

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

#### Module Search Path

- The directory from which the input script was run (the script resides) or the current directory if the interpreter is being run interactively
- The list of directories contained in the `PYTHONPATH` environment variable, if it is set. (The format for `PYTHONPATH` is OS-dependent but should mimic the `PATH` environment variable.)
- An installation-dependent list of directories configured at the time Python is installed

### Symbol Table

Symbol Table holds the variable name, address and types. Programming Language like python support nested blocks. Symbol Tables are created Blockwise hierarchically.

![Symbol-Table-TutorialsPoint](https://www.tutorialspoint.com/compiler_design/images/symbol_table.jpg)

#### Variables in Python are referenced to objects

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

## Best Practices

### Naming

- Variables, functions, methods, packages, modules
  - `lower_case_with_underscores`
- Classes and Exceptions
  - `CapWords`
- Protected methods and internal functions
  - `_single_leading_underscore(self, ...)`
- Private Methods
  - `__double_leading_underscore(self, ...)`
- Constants
  - `ALL_CAPS_WITH_UNDERSCORES`

### Module and Package importing Order

1. System Imports
2. Third-Party Imports
3. Local Source Tree Imports

## References

### Reserved Classes of Identifiers

1. `_*` Not imported by from module import \*
2. `__*__` System Defined Names
3. `__*` class-private names.

### is vs equal

1. `==` checks for equality
2. `is` checks for identity

```python
a = [1,2,3]
b = a
a == b  # contents of a and b are equal ? => True
a is b # is a and b pointing to the same object => TRUE
c = list(a)
a == c # True
a is c # False
```

### site packages vs dist packages

- **site-packages** - installed by pip or python
- **dist-packages** - installed by system's package-manager like `apt`.

## Resources

### Modules and Packages Importing

- [Real Python Module and Package Intro](https://realpython.com/python-modules-packages)
- [Symbol Table](https://eli.thegreenplace.net/2010/09/18/python-internals-symbol-tables-part-1)

## Running the tests

```bash
pytest -svv
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

- [pytest](./examples/pytest)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

- **Alamin Mahamud** - _Initial work_ - [alamin.rocks](https://alamin-rocks.herokuapp.com)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration - vinta and other awesome repo guys.
