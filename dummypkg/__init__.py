"""This package does not do anything, it simply demonstrates the structure of packages that can be documented by ``gendocs``. Note how the heading of this page uses the ``__displayname__`` attribute found in the ``__init__.py``; display names can be set for any element being documented
"""
from .module import *
from .moremod import *
from .subpkg import *

__displayname__ = 'Dummy Package'
