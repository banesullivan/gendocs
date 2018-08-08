"""This provides all of the functionality behind ``gendocs`` and contains the ``Generator`` class which is what you will need to use if you would like to start automatically documenting your packages.

Conventions
-----------

In order for ``gendocs`` to work properly, we have re-definded the idea of `packages` and `modules` for the sake of ``gendocs``. A package can contain just about anything: classes, functions, modules, sub-module, etc.; while a module in the traditional sense can do the same, we re-define modules to not contain any further sub-modules. This re-definition allows ``gendocs`` to mimic the structure of a Python package and automatically generate documentation pages containing the docstrings for the package!

What to Include
^^^^^^^^^^^^^^^

For ``gendocs`` to work, every module being documented MUST contain an ``__all__`` varaible defining what is available to be documented. This varaible ensures ``gendocs`` does not recurse through external packages you might use internally.

Some optional variables:

- ``__displayname__`` (``str``): include this attribute to change how the heading for any documented element is displayed
- ``__category__`` (``str``): if any documented element contains this attribute, a statics table will be generated n the home page to count occurences of various categories.


A Simple Use Case
-----------------

If you simply just want to put up the documentation for your package, then set up sphinx documentation using ``sphinx-quickstart`` (`details`_) and stop after you've generated a new ``conf.py``. Edit the parameters of your configuration file appropriately and then add the following somewhere near the top:

.. _details: http://www.sphinx-doc.org/en/1.7/tutorial.html

.. code-block:: python

    # Import the package to document:
    import wonderfulpackage

    # Automatically generate documentation pages
    from gendocs import Generator
    Generator().DocumentPackages(wonderfulpackage)


That's all you have to do! Now you can push your changes to a continuous integration like ReadTheDocs and have your entire package automatically documented.


Sophisticated Use Case
----------------------

Private Members
^^^^^^^^^^^^^^^

Its worth noting that you can control how private features are ducumented by passing an argument to the the ``DocumentPackages`` method:

.. code-block:: python

    # Import the package to document:
    import wonderfulpackage

    # Automatically generate documentation pages and show private members
    from gendocs import Generator
    Generator().DocumentPackages(wonderfulpackage, showprivate=True)


Custom Homepage
^^^^^^^^^^^^^^^

To use your own homepage to provide a project overview then create a ``.rst`` file containing the content for your homepage and pase the relative file name to the ``DocumentPackages`` method:

.. code-block:: python

    # Import the package to document:
    import wonderfulpackage

    # Automatically generate documentation pages and show private members
    from gendocs import Generator
    gen = Generator()
    gen.DocumentPackages(
                         wonderfulpackage,
                         index_base='../index_base.rst',
                         showprivate=True
                        )


"""


__all__ = [
    'Classifier',
    'Generator',
]

import inspect
import os
import sys
import shutil
import properties

appIndex = '''

.. toctree::
   :maxdepth: 3
   :caption: PVGeo:
'''


SAMPLE_INDEX = """
Welcome to the docs!
********************

.. image:: https://img.shields.io/badge/docs%20by-gendocs-blue.svg
   :target: https://gendocs.readthedocs.io/en/latest/?badge=latest)
   :alt: Documentation Built by gendocs

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
        und = '='*len(heading)
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
        und = '-'*len(heading)
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
        und = '-'*len(heading)
        return r'''

%s
%s

.. autofunction:: %s

''' % (heading, und, name)






class Generator(properties.HasProperties):
    """An object to assist in the automatic generation of documentation pages
    for a given package. These methods iterate over a package and document each
    submodule as their own page. This class handles packages and modules in a very specific manner:
    - `packages` contain modules, classes, and functions
    - `modules` cannot contain sub-modules but only classes and functions
    """
    def __init__(self, **kwargs):
        properties.HasProperties.__init__(self, **kwargs)
        self.__stats = None
        # A dictionary to keep track of Statistics base on the ``__category__`` variable of any documented element.
        self.__categories = dict()


    path = properties.String(
            'The top level directory to store all documentation content.',
            default='content'
            )


    def _GenerateStaticsTable(self, title='Current Statistics'):
        """Generates a statics table based on set categories"""
        if len(self.__categories.keys()) < 1:
            return ''
        d = self.__categories
        keys = sorted(d.keys())
        cats = ', '.join(['"%s"' % k for k in keys])
        vals = ', '.join(['%d' % d[k] for k in keys])

        return r'''

%s
%s

.. csv-table::
   :header: %s

   %s

''' % (title, '-'*len(title), cats, vals)

    def _ProduceSingleContent(self, mod, showprivate=False):
        """An internal helper to create a page for a single module. This will
        automatically generate the needed RSF to document the module
        and save the module to its own page in its appropriate location.

        Args:
            mod (module): The single module to document as its own page
            showprivate (bool): A flag for whether or not to display private members

        Returns:
            str: The file name ready to be appended to a toctree
        """
        try:
            all = mod[1].__all__
        except AttributeError:
            raise RuntimeError('Module (%s) MUST have `__all__` defined.' % mod[1].__name__)
        try:
            name = mod[1].__displayname__
        except AttributeError:
            name = mod[0]
        try:
            category = mod[1].__category__
            self.__categories.setdefault(category, 0)
            self.__categories[category] += 1
        except AttributeError:
            pass
        feats = inspect.getmembers(mod[1])
        fname = 'content/' + mod[1].__name__.replace('.', '/').replace(' ', '-')+'.rst'
        feats = [f for f in feats if f[0] in all and (showprivate or not f[0][0:1] == '_')]
        with open(fname, 'w') as fid:
            fid.write(Classifier.GetModuleText(name, mod[1].__name__, showprivate=showprivate))

            for f in feats:
                # Check for a __displayname__
                if inspect.isclass(f[1]) or inspect.isfunction(f[1]):
                    try:
                        featname = f[1].__displayname__
                    except AttributeError:
                        featname = f[1].__name__
                    try:
                        category = f[1].__category__
                        self.__categories.setdefault(category, 0)
                        self.__categories[category] += 1
                    except AttributeError:
                        pass
                    # Make the auto doc rst
                    if inspect.isclass(f[1]):
                        fid.write(Classifier.GetClassText(featname, '%s.%s' % (mod[1].__name__, f[1].__name__), showprivate=showprivate))
                    elif inspect.isfunction(f[1]):
                         fid.write(Classifier.GetFunctionText(featname, '%s.%s' %  (mod[1].__name__, f[1].__name__)))

            fid.close()
        return '\n   %s' % (fname.split('/')[-1])



    def _ProduceContent(self, mods, showprivate=False):
        """An internal helper to create pages for several modules that do not have nested modules.
        This will automatically generate the needed RSF to document each module module
        and save the module to its own page appropriately.

        Args:
            mods (module): The modules to document that do not contain nested modules
            showprivate (bool): A flag for whether or not to display private members

        Returns:
            str: The file names ready to be appended to a toctree
        """
        result = ''
        nestedresult = ''

        # For each module
        for mod in mods:
            # Test to see if module to document has an __all__ variable
            try:
                all = mod[1].__all__
            except AttributeError:
                raise RuntimeError('Module (%s) MUST have `__all__` defined.' % mod[1].__name__)
            if not showprivate and mod[0][0:1] == '_':
                continue
            if mod[0][0:2] == '__': #and not showprivate
                continue
            result += self._ProduceSingleContent(mod, showprivate)
        return result




    def _MakePackagePages(self, package, showprivate=False, nested=False):
        """An internal helper to generate all of the pages for a given package

        Args:
            package (module): The top-level package to document
            showprivate (bool): A flag for whether or not to display private members
            nested (bool): Foor internal use ONLY

        Returns:
            str: The file names ready to be appended to a top-level toctree
        """

        def checkNoNested(mod):
            try:
                all = mod.__all__
            except AttributeError:
                return False
            mems = inspect.getmembers(mod, inspect.ismodule)
            mems = [m for m in mems if m[0] in mod.__all__]

            if len(mems) > 0:
                return False
            return True

        # Get package module members
        mods = inspect.getmembers(package, inspect.ismodule)
        # Split into modules and sub-packages
        nmods, pvt, npkgs = [], [], []
        for mod in mods:
            # Deal with private modules
            if checkNoNested(mod[1]):
                if mod[0][0] == '_': pvt.append(mod)
                else: nmods.append(mod)
            else: npkgs.append(mod)
        if showprivate: nmods += pvt


        # for each member that has a nested module
            # recurse and keep track of index files for that package
        files = []
        ignore = []
        for pkg in npkgs:
            pt = '%s/%s/%s' % (self.path, package.__name__.replace('.', '/'), pkg[1].__name__.split('.')[-1])
            if os.path.exists(pt): shutil.rmtree(pt)
            os.makedirs(pt)
            ignore += inspect.getmembers(pkg[1])
            f = self._MakePackagePages(pkg[1], showprivate=showprivate, nested=True)
            files.append(f.split(package.__name__.replace('.', '/')+'/')[1])

        if nested:
            try:
                name = package.__displayname__
            except AttributeError:
                name = package.__name__
            # Create index file here
            index = r'''
%s
%s

.. toctree::
   :maxdepth: 5
    ''' % (name, '*' * len(name))
            # include sub packages first
            index += '\n   '.join(files)
            # then include modules
            index += '\n   ' + self._ProduceContent(nmods, showprivate=showprivate)
            findex = 'content/%s/index.rst' % (package.__name__.replace('.', '/'))

            # Write the file
            with open(findex, 'w') as f:
                if package.__doc__: f.write(package.__doc__)
                f.write(index)

            # return filename for index file at package level
            return '\n   ' + findex

        # Not nested: return all files
        names = '\n   %s/%s/' % ( self.path, package.__name__.replace('.', '/'))
        nmods = [m for m in nmods if m not in ignore]
        return names.join(self._ProduceContent(nmods, showprivate=showprivate).split('\n   ')+files)



    def _DocPackageFromTop(self, packages, showprivate=False):
        """Generates all of the documentation for given packages and
        appends new tocrees to the index. All documentation pages will be under the
        set relative path.

        Args:
            packages (list(module)): A package or list of packages that contain submodules to document
            showprivate (bool): A flag for whether or not to display private members

        Returns:
            str: The new content to append to the index
        """
        appIndex = ''
        if not isinstance(packages, list):
            packages = [packages]

        if os.path.exists('content'):
            shutil.rmtree('content')
        os.makedirs('content')

        # Iterate over each package and generate appropriate pages
        for i in range(len(packages)):
            # The package to document and its path
            package = packages[i]
            try:
                name = package.__displayname__
            except AttributeError:
                name = package.__name__
            # Each package at top level gets its own toctree
            appIndex += r'''

.. toctree::
   :maxdepth: 5
   :caption: %s:
''' % (package.__name__)
            # Make sure paths are ready
            path = 'content/%s' % name
            if os.path.exists(path):
                shutil.rmtree(path)
            os.makedirs(path)

            # Check if there is top level documentation
            if package.__doc__:
                # Get metadata
                meta = 'About %s\n%s\n' % (name, '='*len('About ' + name))
                author = getattr(package, "__author__", None)
                license = getattr(package, "__license__", None)
                copyright = getattr(package, "__copyright__", None)
                version = getattr(package, "__version__", None)
                if author: meta += '\n* Author: %s' % author
                if license: meta += '\n* License: %s' % license
                if copyright: meta += '\n* Copyright: %s' % copyright
                if version: meta += '\n* Version: %s' % version
                about = '%s/%s' % (path, 'about.rst')
                with open(about, 'w') as f:
                    f.write('%s\n\n' % meta)
                    f.write(package.__doc__)
                appIndex += '\n   %s' % about

            appIndex += self._MakePackagePages(package, showprivate=showprivate)

        # Return the new content to append
        return appIndex


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

    # TODO remove path arg
    def DocumentPackages(self, packages, index_base=None, showprivate=False):
        """This is the high level API to use to generate documentation pages for any given package(s).

        Args:
            packages (list(module)): A list of packages that contain submodules to document
            index_base (str): The index page file name. This content will be appended
            showprivate (bool): A flag for whether or not to display private members
        """
        if index_base is None:
            index = SAMPLE_INDEX
        else:
            index = self.OpenIndex(index_base)
        app = self._DocPackageFromTop(packages, showprivate=showprivate)
        index += self._GenerateStaticsTable()
        index += """
.. toctree::
   :hidden:

   self

"""
        self.WriteIndex(index + app)
        return None
