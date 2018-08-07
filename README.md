# Automatic Documentation Generator

This is a Python package for automatically building the documentation pages to document a given Python package for Sphinx.
Currently, this generator only handles packages with one level of submodules and each submodule must have an `__all__` defined to declare what gets documented.

Want to what this produces? Head over to the `gendocs` [documentation]() for a preview!


# Usage

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
