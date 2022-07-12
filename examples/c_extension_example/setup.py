"""Setup to build the C-extension library modules"""

# pylint: disable=line-too-long
# pylint: disable=wrong-import-order

# importing setuptools is important to avoid getting the error: "Unable to find vcvarsall.bat" when compiling the .pyx files into Python importable files.
# Note: it is important to import setuptools before distutils, because it monkeypatches the distutils library to avoid the following error:
# "error: each element of 'ext_modules' option must be an Extension instance or 2-tuple"
import setuptools  # type: ignore # pylint: disable=unused-import

from distutils.core import Extension, setup


setup(
    name="lib",
    version="1.0.0",
    description="Fibonacci number calculation library module",
    ext_modules=[Extension("lib", sources=["lib.c"], include_dirs=["src"])],
)
