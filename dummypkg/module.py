"""``module`` is a module at the top level of the ``dummypkg`` package which contains no submodules but only classes, functions, and other not module like code.

.. admonition:: Note

    Note that only what is defined in this module's ``__all__`` list is what is accessible and what get's documented.
    Whithout an ``__all__`` the documentation build will fail.

"""

__all__ = [
    'foo',
    '_privatefoo',
]

__displayname__ = 'Top Level Module'

class foo(object):
    """This a public class that is accessible and documented"""
    def __init__(self):
        print('foo')


class _privatefoo(object):
    """This is a private class because of the ``_`` prefix, yet it is still
    documented because we have the ``showprivate`` variable of the ``Generator``
    in our ``conf.py`` enabled.
    """
    def __init__(self):
        print('private foo')

    def doStuff(self, arg1, arg2):
        """A method to do some wonderful stuff

        Args:
            arg1 (int): a wonderful number
            arg2 (list(str)): the list to access

        Returns:
            str: the string at index ``arg1`` of ``arg2``
        """
        return arg2[arg1]

    @staticmethod
    def _privateAndStatic(foo):
        """This is private and static: it sorts dictionary keys.

        Args:
            foo (dict): a dictionarty to use

        Returns:
            list: The dictionary keys sorted
        """
        return [k for k in sorted(foo.keys())]
