# Generate Documentation Automatically

[![PyPI](https://img.shields.io/pypi/v/gendocs.svg)](https://pypi.org/project/gendocs/) [![Build Status](https://travis-ci.org/banesullivan/gendocs.svg?branch=master)](https://travis-ci.org/banesullivan/gendocs) [![Documentation Status](https://readthedocs.org/projects/gendocs/badge/?version=latest)](https://gendocs.readthedocs.io/en/latest/?badge=latest)


This is a Python package for automatically building the documentation pages to document a given Python package for Sphinx.
Currently, this generator only handles packages with one level of submodules and each submodule must have an `__all__` defined to declare what gets documented.

Want to see what this produces? Head over to the `gendocs` [documentation](https://gendocs.readthedocs.io/en/latest/) for a preview!

# Get Started

Install `gendocs` from PyPI:
```bash
$ pip install gendocs
```


## Usage

This generator is built for Sphinx (RST) documentation.
To document your package, setup sphinx and a `conf.py` then add the following
somewhere near the top of your `conf.py`:

```py

# Import the package to document:
import wonderfulpackage
# Automatically generate documentation pages
from gendocs import Generator
Generator.DocumentPackages(wonderfulpackage)

```

Note that you can also set up a base index file in your project for the `Generator`
to append if you'd like to include a brief overview of the package.
We keep ours in the top level of the docs directory and pass the filename to the
`DocumentPackages` method.


# Projects Using `gendocs`

- [ESPA Tools](https://espatools.readthedocs.io/en/latest/?badge=latest): A Python package for simple loading of Landsat imagery as NumPy arrays
- [PVGeo](http://docs.pvgeo.org): A Python package for visualizing geophysical data in VTK and ParaView


# Are you using `gendocs`?

If your project generates documentation automatically, please add a badge to your project to let people know! We hope that these badges will stir curiosity, involvement, and community contributions to the `gendocs` package.

Markdown:

```text
[![Documentation Built by gendocs](https://img.shields.io/badge/docs%20by-gendocs-blue.svg)](https://gendocs.readthedocs.io/en/latest/?badge=latest)
```

RST / Sphinx:

```text
.. image:: https://img.shields.io/badge/docs%20by-gendocs-blue.svg
   :target: https://gendocs.readthedocs.io/en/latest/?badge=latest)
   :alt: Documentation Built by gendocs

```
