# How To

## Create a virtual environment

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

# change `which python2.*` to python3 if needed
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
mkvirtualenv <virtual-environment-name>
workon <virtual-environment-name>
```
