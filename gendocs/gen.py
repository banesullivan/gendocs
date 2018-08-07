__all__ = [
    'Classifier',
    'Generator',
]

import inspect
import os
import sys
import shutil

appIndex = '''

.. toctree::
   :maxdepth: 3
   :caption: PVGeo:
'''


SAMPLE_INDEX = """
Welcome to the docs!
====================

This website hosts the code documentation for a wonderful Python package.
This documentation was built using `gendocs`_, an automatic documentation pages
generator so developers can focus on their work and not worry about including
new features in their documentation.


.. _gendocs: https://github.com/banesullivan/gendocs/

.. toctree::
   :hidden:

   self



"""


############

class Classifier(object):

    @staticmethod
    def GetModuleText(heading, name, showprivate=False):
        """Returns the needed text to automatically document a module in RSF/sphinx"""
        und = '-'*len(heading)
        if showprivate:
            opts = ':private-members:'
        else:
            opts = ''
        return r'''

%s
%s

.. automodule:: %s
    %s

''' % (heading, und, name, opts)

###############################################################################

    @staticmethod
    def GetClassText(heading, name, showprivate=False):
        """Returns the needed text to automatically document a class in RSF/sphinx"""
        und = '^'*len(heading)
        if showprivate:
            opts = ':private-members:'
        else:
            opts = ''
        return r'''

%s
%s

.. autoclass:: %s
    :show-inheritance:
    :members:
    :undoc-members:
    %s

''' % (heading, und, name, opts)

###############################################################################


    @staticmethod
    def GetFunctionText(heading, name):
        """Returns the needed text to automatically document a function in RSF/sphinx"""
        und = '^'*len(heading)
        return r'''

%s
%s

.. autofunction:: %s

''' % (heading, und, name)



class Generator(object):
    """An object to assist in the automatic generation of documentation pages
    for a given package. These methods iterate over a package and document each
    submodule as their own page.
    """

    @staticmethod
    def _ProduceContent(mods, path, modname, showprivate=False):
        """An internal helper to create pages for a module. This will automatically
        generate the needed RSF to document each submodule module and save each
        sumbodule to its own page under the given path.

        Args:
            mods (module): The module to document as its own page
            path (str): The relative directory name to save the page
            modname (str): The displayname of the module
            showprivate (bool): A flag for whether or not to display private members

        Returns:
            str: A tocree to append to the index page for navigation
        """
        appIndex = '''

.. toctree::
   :maxdepth: 3
   :caption: %s:
    ''' % modname
        for mod in mods:
            if not showprivate and mod[0][0:1] == '_':
                continue
            if mod[0][0:2] == '__': #and not showprivate
                continue
            try:
                name = mod[1].__displayname__
            except AttributeError:
                name = mod[1].__name__
            try:
                all = mod[1].__all__
            except AttributeError:
                raise RuntimeError('Each module MUST have `__all__` defined.')
            feats = inspect.getmembers(mod[1])
            fname = name.replace(' ', '-')+'.rst'
            appIndex += '\n   %s/%s' % (path, fname)
            feats = [f for f in feats if f[0] in all and (showprivate or not f[0][0:1] == '_')]
            with open('./%s/%s' % (path, fname), 'w') as fid:
                fid.write(Classifier.GetModuleText(name, mod[1].__name__, showprivate=showprivate))

                for f in feats:
                    # Check for a __displayname__
                    if inspect.isclass(f[1]) or inspect.isfunction(f[1]):
                        try:
                            featname = f[1].__displayname__
                        except AttributeError:
                            featname = f[1].__name__
                        # Make the auto doc rst
                        if inspect.isclass(f[1]):
                            fid.write(Classifier.GetClassText(featname, '%s.%s' % (mod[1].__name__, f[1].__name__), showprivate=showprivate))
                        elif inspect.isfunction(f[1]):
                             fid.write(Classifier.GetFunctionText(featname, '%s.%s' %  (mod[1].__name__, f[1].__name__)))

                fid.close()
        return appIndex

    @staticmethod
    def MakePages(packages, index, path='pages', showprivate=False):
        """Generates all of the documentation for given packages and
        appends new tocrees to the index. All documentation pages will be under the
        set relative path.

        Args:
            packages (list(module)): A list of packages that contain submodules to document
            index (str): The index page content to append
            path (str): The relative directory name to save the page
            showprivate (bool): A flag for whether or not to display private members

        Returns:
            str: The new index page contents containing needed tocrees
        """
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)
        appIndex = ''
        if not isinstance(packages, list):
            packages = [packages]
        for module in packages:
            mods = inspect.getmembers(module, inspect.ismodule)
            nmods, pvt = [], []
            for mod in mods:
                if mod[0][0] == '_': pvt.append(mod)
                else: nmods.append(mod)
            nmods += pvt
            appIndex += Generator._ProduceContent(nmods, path, module.__name__, showprivate=showprivate)

        return index + appIndex

    @staticmethod
    def OpenIndex(filename):
        with open('../index_base.rst', 'r') as fid:
            index = fid.read()
            fid.close()
        return index

    @staticmethod
    def WriteIndex(index):
        with open('./index.rst', 'w') as fid:
            fid.write(index)
        return None

    @staticmethod
    def DocumentPackages(packages, index_base=None, showprivate=False):
        """This is the high level API to use to generate documentation pages for any given package(s).

        Args:
            packages (list(module)): A list of packages that contain submodules to document
            index_base (str): The index page file name. This content will be appended
            showprivate (bool): A flag for whether or not to display private members
        """
        if index_base is None:
            index = SAMPLE_INDEX
        else:
            index = Generator.OpenIndex(index_base)
        index = Generator.MakePages(packages, index, showprivate=showprivate)
        Generator.WriteIndex(index)
        return None
