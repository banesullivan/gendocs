"""Here is another module to demonstrate that that each module gets its own page!"""

__all__ = [
    'DoSomething'
]

__displayname__ = 'Another Module'

class DoSomething(object):
    """This a class to do ``something``. Give it ``something`` to do!

    Args:
        something (callable): A callable object to act on
        kwargs (dict): Arguments to pass to the ``something`` to do

    Return:
        object: returns the restult of doing ``something``
    """
    def __init__(self, something, **kwargs):
        self.something = something
        self.args = kwargs
        self.DoIt()

    def DoIt(self):
        """Performs the action

        Return:
            object: returns the restult of doing ``something``
        """
        return self.something(**kwargs)
