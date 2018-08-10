Generate Documentation Automatically
====================================

.. image:: https://readthedocs.org/projects/gendocs/badge/?version=latest
   :target: https://gendocs.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image :: https://img.shields.io/pypi/v/gendocs.svg
   :target: https://pypi.org/project/gendocs/
   :alt: PyPI

.. image :: https://travis-ci.org/banesullivan/gendocs.svg?branch=master
   :target: https://travis-ci.org/banesullivan/gendocs
   :alt: Build Status

.. image :: https://img.shields.io/github/stars/banesullivan/gendocs.svg?style=social&label=Stars
   :target: https://github.com/banesullivan/gendocs
   :alt: GitHub


This is a Python package for automatically building the documentation pages to
document a given Python package using Sphinx.
``gendocs`` allows users to keep all of their documentation directly within their
packages as pages are generated directly from the docstrings in the code!

Connections
-----------

Want to see examples? Check out one of the following projects which uses ``gendocs``:

- `PVGeo`_: A Python package for visualizing geophysical data in VTK and ParaView
- `ESPA Tools`_: A Python package for simple loading of Landsat imagery as NumPy arrays


.. _ESPA Tools: https://espatools.readthedocs.io/en/latest/
.. _PVGeo: http://docs.pvgeo.org


Get Started
-----------

Install `gendocs` from PyPI:

.. code-block:: bash

    $ pip install gendocs



Usage
^^^^^

This generator is built for Sphinx (RST) documentation.
To document your package, setup sphinx and a ``conf.py`` then add the following
somewhere near the top of your ``conf.py``:

.. code-block:: python

    # Import the package to document:
    import wonderfulpackage

    # Automatically generate documentation pages
    from gendocs import Generator
    Generator().DocumentPackages(wonderfulpackage)

That's it! That code block above is all you need to do to fully document your package(s). Now you can build the Sphinx documentation and all docs pages will be automatically generated.


.. admonition:: Remove the `Edit on GitHub` Button
   :class: warning

    Be sure to remove the `Edit on GitHub` link from your project by following `these steps`_.

    .. _these steps: https://docs.readthedocs.io/en/latest/guides/remove-edit-buttons.html


.. admonition:: Make Your Own Homepage
   :class: note

    Note that you can also set up a base index file in your project for the ``Generator``
    to append if you'd like to include a brief overview of the package.
    We simply pass the filename of our README to the
    ``DocumentPackages`` method.


Let People Know
---------------

If your project generates documentation automatically, please add a badge to your project to let people know! We hope that these badges will stir curiosity, involvement, and community contributions to the ``gendocs`` package.

Markdown:

.. code-block:: text

    [![Documentation Built by gendocs](https://img.shields.io/badge/docs%20by-gendocs-blue.svg)](https://gendocs.readthedocs.io/en/latest/)


RST / Sphinx:

.. code-block:: text

    .. image:: https://img.shields.io/badge/docs%20by-gendocs-blue.svg
       :target: https://gendocs.readthedocs.io/en/latest/
       :alt: Documentation Built by gendocs


Contribute
----------
Check out ``gendocs`` of `GitHub`_ to Contribute and make automatic documentation even better!

.. _GitHub: https://github.com/banesullivan/gendocs
