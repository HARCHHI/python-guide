# Python project initial guide

a simple guild project to help you build a python develop environment

## Initial project

`python3 -m venv .venv`

## Install

### Tricky points
    **WARRING**

    Never install any develop tools in global environment.
    Many develop tools(pytest) resolve project config automatically.
    If install any

### Dev deps

Install all you need when you maintain your project.

`pip install -r requirements-dev.txt`
`pip install -e .`

### Production deps

This command only install production dependencies.

`python setup.py install`


## Folder structure

Following structure of flask.
More detail explained in this [blog](https://blog.ionelmc.ro/2014/05/25/python-packaging)

```
Project/
├─ src
│  └─ packagename
│     ├─ __init__.py
│     └─ ...
├─ tests
│  └─ ...
└─ setup.py
```

## Tech stack

Every configuration you need has been committed.

This is list of technologies using in this reop.
* environment manager
  * venv(or virtualenv): Isolating host environment and proejct.
* test
  * tox: Automate and standardize testing tool.
  * pytest: The most famous test framework in python.
* lint
  * flake8: Light lint tool.
  * mypy
* package manager
  * setuptools(setup.py, standard lib, for production)
  * pip requirements file(for development)
* architecture
  * ABC(Abstract Base Classes, standard lib)
  * dataclasses(standard lib)
* CI
  * TBD...
* docs
  * pyDoc
