"""This is a module in the ``subpkg`` sub-package of ``dummypkg``.
This module has its own classes, functions, etc. to be documented.
"""

__all__ = [
    'CleanGoop',
    'raiseErr',
]

__displayname__ = 'Goop Module'

class CleanGoop(object):
    """This is a class dedicated to cleaning goop!

    Args:
        toclean (object): the goop to be cleaned
    """
    def __init__(self, toclean):
        print('Goop is being cleaned...')
        self.goop = toclean
        self.Clean()

    def Clean(self):
        return self.goop is not None


def raiseErr(msg='ERROR: bad coder!'):
    raise Exception(msg)
