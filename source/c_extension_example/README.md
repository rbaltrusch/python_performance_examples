# C-extension example

This example speeds up the library function considerably by implementing it completely in C as a C-extension for Python. It runs about 10 times faster than the base example written in vanilla Python.

Note that this example will require an installed C-compiler (on Windows, Microsoft C/C++ Build Tools may need to be downloaded, as well the Native development tools option in the Visual Studio Python development workload section). Compiling the code means, however, that the final distributable is now platform specific and separate distributions must be made for, e.g. Windows, Mac OS and Linux.

# How to run example

From the project root directory, change into this example folder and install all dependencies:

```
cd source/c_extension_example
python -m pip install requirements.txt
```

Compile the C-extension files specified in the `setup.py` file (with the `-i` flag, making them importable in Python):
```
python setup.py build_ext -i
```

Finally, run the `src` python package:
```
python -m src
```

## Windows C-extension compilation

Note that this example will require:
- an installed C-compiler
- Microsoft C/C++ Build Tools
- Visual Studio Python development workload (only Native development tools option are required)
- You may need to restart your machine before being able to run the setup.py without errors.

For more information and troubleshooting, check out [this blogpost](https://devblogs.microsoft.com/python/unable-to-find-vcvarsall-bat/).
