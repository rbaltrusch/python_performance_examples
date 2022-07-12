# Cython library

This example defines an external library function in lib.py using Cython, which, after compilation, can be imported in regular python code. It runs about times faster than the base example written in vanilla Python.

# How to run example

From the project root directory, change into this example folder and install all dependencies

```
cd examples/numba_example
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

