"""``subpkg`` demonstrates that sub-packages can be automatically documented as
``gendocs`` recurses into the module being documented to reproduce its file
structure as documentation.
"""

__displayname__ = 'Sub-Package'

from .goop import *
