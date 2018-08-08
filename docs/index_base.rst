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

This is a Python package for automatically building the documentation pages to
document a given Python package for Sphinx.

Connections
-----------

Want to see what this produces? Check out one of the following projects which uses ``gendocs``:

- `ESPA Tools`_: A Python package for simple loading of Landsat imagery as NumPy arrays
- `PVGeo`_: A Python package for visualizing geophysical data in VTK and ParaView


.. _ESPA Tools: https://espatools.readthedocs.io/en/latest/?badge=latest)
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


.. admonition:: Note

    Note that you can also set up a base index file in your project for the ``Generator``
    to append if you'd like to include a brief overview of the package.
    We keep ours in the top level of the docs directory and pass the filename to the
    ``DocumentPackages`` method.


Let People Know
---------------

If your project generates documentation automatically, please add a badge to your project to let people know! We hope that these badges will stir curiosity, involvement, and community contributions to the ``gendocs`` package.

Markdown:

.. code-block:: text

    [![Documentation Built by gendocs](https://img.shields.io/badge/docs%20by-gendocs-blue.svg)](https://gendocs.readthedocs.io/en/latest/?badge=latest)


RST / Sphinx:

.. code-block:: text

    .. image:: https://img.shields.io/badge/docs%20by-gendocs-blue.svg
       :target: https://gendocs.readthedocs.io/en/latest/?badge=latest)
       :alt: Documentation Built by gendocs


Contribute
----------
Check out ``gendocs`` of `GitHub`_ to Contribute and make automatic documentation even better!

.. _GitHub: https://github.com/banesullivan/gendocs
