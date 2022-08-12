"""Setup to build the Cython library modules"""

import os
from distutils.core import setup

# importing setuptools is important to avoid getting the error: "Unable to find vcvarsall.bat" when compiling the .pyx files into Python importable files.
import setuptools  # type: ignore # pylint: disable=unused-import
from Cython.Build import cythonize  # type: ignore

# This sets the CC environment variable to g++,
os.environ["CC"] = "g++"

setup(
    ext_modules=cythonize("**/*.pyx"),  # type: ignore
)
