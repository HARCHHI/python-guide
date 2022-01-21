# Python project initial guide

a simple guild project to help you build a python develop environment

## Initial project

`python3 -m venv .venv`

## Install

### Tricky points
    **WARRING**

    Never install any develop tools in global environment.
    Many develop tools(pytest) resolve project configuration automatically.
    Using those tools from global path might curse some problem.

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


## Tips

### Naming styles(PEP8)


Type	|Naming Convention	|Examples
----|:---:|:---
Function |Use a lowercase word or words. Separate words by underscores to improve readability.	|function, my_function
Type Variable|Use CapWords preferring short names. It is recommended to add suffixes _co or _contra to the variables used to declare covariant or contravariant behavior correspondingly|T, AnyStr, Num
Variable	|Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.	|x, var, my_variable
Class	|Start each word with a capital letter. Do not separate words with underscores. This style is called camel case.	|Model, MyClass
Method	|Use a lowercase word or words. Separate words with underscores to improve readability.	class_method, method Constant	Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.|CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT
Module	|Use a short, lowercase word or words. Separate words with underscores to improve readability.	|module.py, my_module.py
Package	|Use a short, lowercase word or words. Do not separate words with underscores.	|package, mypackage
