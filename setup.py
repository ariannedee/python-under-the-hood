"""
For local installation:
$ pip install setuptools  <-- if using Python 3.12+
$ python setup.py build_ext --inplace

This will:
- Add a build folder with C-extension files (.so and .o)
- Put a copy of the .so file in the project root directory
  - This is what will load when you import xyz

>>> import xyz
>>> xyz.echo('Hello world')  # Will print to console twice

*Note* this is just a minimal setup to get something working
"""
from setuptools import setup, Extension

xyz_module = Extension('xyz',
                       sources=['Examples/xyzmodule.c'])
setup(name='xyz',
      version='0.0.1',
      description='This is an example package with a C extension',
      ext_modules=[xyz_module])
