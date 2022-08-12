# Jit-acceleration using numba

The accelerated code using the numba Just-In-Time (JIT) compiler should run about 3 times faster than the vanilla Python code in the base example. Note that the first time that this example is run may take a lot more time than subsequent runs due to the JIT compilation time.

# How to run example

From the project root directory, change into this example folder, install all dependencies, then run the `src` python package:

```
cd source/numba_example
python -m pip install requirements.txt
python -m src
```
