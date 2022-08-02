# Cython library

This example defines an external library function in lib.py using Cython, which, after compilation, can be imported in regular python code. It runs about 4-5 times faster than the base example written in vanilla Python.

Note that this example will require an installed C-compiler (on Windows, Microsoft C/C++ Build Tools may need to be downloaded too). Compiling the code means, however, that the final distributable is now platform specific and separate distributions must be made for, e.g. Windows, Mac OS and Linux.

# How to run example

From the project root directory, change into this example folder and install all dependencies:

```
cd examples/cython_example
python -m pip install requirements.txt
```

Compile the Cython .pyx files specified in the `setup.py` file (with the `-i` flag, making them importable in Python):
```
python setup.py build -i
```

Finally, run the `src` python package:
```
python -m src
```

