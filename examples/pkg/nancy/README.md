# NANCY - A Python Package

```
.
├── build                                                # build package information
├── dist                                                 # contains .whl file
    							 # install directly using pip install *.whl
├── LICENSE                                              # LICENSE - information  
├── nancy						 # original script  
├── nancy.egg-info					 # egg package -
    							 # compiled bytecode
							 # pkg information, dep links
							 # and captures the info used by the setup.py test command when running tests
├── README.md
└── setup.py

```

### Install on your local machine

``` shell
pip install ./dist/*.whl
```

### Upload on pip

create a `.pypirc` on `$HOME`.

```
[distutils] 
index-servers=pypi
[pypi] 
repository = https://upload.pypi.org/legacy/ 
username = alamin-mahamud
```

```shell
python3 -m twine upload dist/*
```