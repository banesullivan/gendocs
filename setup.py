"""gendocs: automatically build the documentation pages to document a given Python package for Sphinx
"""

import setuptools

__version__ = '0.1.0'

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="gendocs",
    version=__version__,
    author="Bane Sullivan",
    author_email="banesullivan@gmail.com",
    description="Automatic documentation pages generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/banesullivan/gendocs",
    packages=setuptools.find_packages(),
    install_requires=[
        'Sphinx>=1.7',
        'properties>=0.5.2',
    ],
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        'Natural Language :: English',
    ),
)
