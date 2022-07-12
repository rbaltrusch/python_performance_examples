/* Library code for the Fibonacci sequence, written as a C-extension for Python.
   Should be compiled using a setup.py file, not directly with a C-compiler.
 */

#define PY_SSIZE_T_CLEAN // recommended by the Python docs

/* Include the C-Python API. Note that the Python.h must be on PATH or
included in the build path of the compiler by specifying its folder with the -I<folder> flag.
*/
#include <Python.h>

static PyObject *
fib(PyObject *self, PyObject *args)
{
    // "unbox" input argument called "limit" to convert it from a Python variable to a C int
    int limit;
    if (!PyArg_ParseTuple(args, "limit", &limit))
    {
        return NULL; // signal an error
    }

    /* Initialises a new Python list and initialise it to [0, 1, 1]
    Note that we have to first "box" values (i.e. convert from C to Python), before adding them to the list.
    */
    PyObject *numbers = PyList_New(3);
    PyList_SetItem(numbers, 0, PyLong_FromLong(0));
    PyList_SetItem(numbers, 1, PyLong_FromLong(1));
    PyList_SetItem(numbers, 2, PyLong_FromLong(1));

    int previous = 1;
    int current = 1;
    while (current < limit)
    {
        current = current + previous;
        previous = current;

        // "Box" The current value to convert it to a Python int, then append it to the numbers Python list.
        PyObject *newElement = PyLong_FromLong(current);
        int status = PyList_Append(numbers, newElement);
        // Decrement the reference count of newElement - since this function owns the newElement variable, we must clean it up to not leak memory.
        Py_DECREF(newElement);

        // A status below 0 means that the list.append failed and that the list must be cleaned up, since this function currently owns the list.
        if (status < 0)
        {
            Py_CLEAR(numbers); // Decrements the reference count of numbers and sets it to NULL
            return NULL;
        }
    }
    return numbers;
}

// Contains information about all method definitions in this file
static PyMethodDef FibLibMethods[] = {
    {"fib", fib, METH_VARARGS, "Calculates all Fibonnacci numbers up to the specified limit, then returns them in a list."}, // Our method definition
    {NULL, NULL, 0, NULL}                                                                                                    // Sentinel value
};

// Contains information about the Python module implemented here
static struct PyModuleDef fibLibModule = {
    PyModuleDef_HEAD_INIT,
    "lib",                                       // name of the module
    "Library code implemented as a C-extension", // module documentation, may be NULL
    -1,                                          // size of the module state, or -1 if it keeps state as global variables
    FibLibMethods,
};

// Initialise the Python module
PyMODINIT_FUNC
PyInit_lib(void)
{
    return PyModule_Create(&fibLibModule);
};
