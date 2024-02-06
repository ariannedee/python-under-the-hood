/* Extending Python with C: https://docs.python.org/3/extending/extending.html
Creates a module named 'xyz' that has a function 'echo' that prints the input to the console twice

To add extension to a Python executable:
1. Move this to cpython/Modules
2. Add "xyz xyzmodule.o" to cpython/Modules/Setup.local
3. Compile Python based on your OS (https://realpython.com/cpython-source-code-guide/)
4. Run Python
  >> import xyz
  >> xyz.echo('hello world')

To install locally (without editing CPython):
$ python setup.py build_ext --inplace
See setup.py for more info
*/

#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *
xyz_echo(PyObject *self, PyObject *args)
{
    const char *string;

    if (!PyArg_ParseTuple(args, "s", &string)) {  // If the positional arguments were invalid
        return NULL;                              // Raise an exception
    }

    printf("%s\n%s\n", string, string);  // Print string out twice

    // Returns None
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef XyzMethods[] = {
    {"echo",  xyz_echo, METH_VARARGS,
     "Print out the text twice."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef xyzmodule = {
        PyModuleDef_HEAD_INIT,
        "xyz",   /* name of module */
        NULL,    /* module documentation, may be NULL */
        -1,      /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    XyzMethods
};

PyMODINIT_FUNC
PyInit_xyz(void)
{
    return PyModule_Create(&xyzmodule);
}
