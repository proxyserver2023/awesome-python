# Awesome Python Examples

Codebase for excellent python project examples.

## Table of Contents

- [Getting Started](#getting-started)
- [Concepts](#concepts)
  - [Metaclass](#metaclass)
  - [Importing Modules and Packages](#importing-modules-and-packages)

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

#### Module Search Path

-  
- 
- 


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

- **Alamin Mahamud** - *Initial work* - [alamin.rocks](https://alamin-rocks.herokuapp.com)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration - vinta and other awesome repo guys.
