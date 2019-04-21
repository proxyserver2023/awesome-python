# Awesome Python Examples

Codebase for excellent python project examples.

## Table of Contents

- [Getting Started](#getting-started)
- [Concepts](#concepts)
  - [Metaclass](#metaclass)

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

## Running the tests

```bash
pytest -ra
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
