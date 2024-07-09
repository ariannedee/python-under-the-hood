"""
vars - https://docs.python.org/3/library/functions.html#vars
  vars(): returns locals()
  vars(obj): returns the __dict__ mapping of attributes of an object

dir - https://docs.python.org/3/library/functions.html#dir
  dir(): returns a list of names in the current scope (keys of locals() dict)
  dir(obj): attempts to return a list of valid attributes for the object (i.e. obj.{attr})
"""
import inspect
from pprint import pprint

import hello


class ClassA:
    att1 = 1

    def __init__(self):
        self.att2 = 2


class ClassB(ClassA):
    att3 = 3

    def __init__(self):
        super().__init__()
        self.att4 = 4


inst_A = ClassA()
inst_B = ClassB()
x = 5


def a_func(y):
    """A function"""
    z = 7
    print('\nlocal vars()')
    pprint(vars())
    print('\nlocal dir()')
    pprint(dir())


# Locals
a_func(6)
a_func.num_calls = 1

# Globals
print('\n--- global vars() ---\n')
pprint(vars())
print('\n--- global dir() ---\n')
pprint(dir(), compact=True)

# Function
print('\n--- vars(a_func) ---\n')
print(vars(a_func))
print('\n--- local dir(a_func) ---\n')
pprint(dir(a_func), compact=True)

# Module
print('\n--- vars(hello) ---\n')
module_dict = vars(hello)
del module_dict['__builtins__']  # Don't display builtins
pprint(module_dict)
print('\n--- local dir(hello) ---\n')
pprint(dir(hello), compact=True)

# Class
print('\n--- vars(ClassA) ---\n')
pprint(vars(ClassA))
print('\n--- dir(ClassA) ---\n')
pprint(dir(ClassA), compact=True)
print('\n--- vars(inst_A) ---\n')
pprint(vars(inst_A))
print('\n--- dir(inst_A) ---\n')
pprint(dir(inst_A), compact=True)

# Subclass
print('\n--- vars(ClassB) ---\n')
pprint(vars(ClassB))
print('\n--- dir(ClassB) ---\n')
pprint(dir(ClassB), compact=True)
print('\n--- getmembers(ClassB) ---\n')
pprint(inspect.getmembers(ClassB))
print('\n--- vars(inst_B) ---\n')
pprint(vars(inst_B))
print('\n--- dir(inst_B) ---\n')
pprint(dir(inst_B), compact=True)
print('\n--- getmembers(inst_B) ---\n')
pprint(inspect.getmembers(inst_B))
print('\n--- getmembers(inst_B) that are routines ---\n')
pprint(inspect.getmembers(inst_B, predicate=inspect.isroutine))
print('\n--- getmembers(inst_B) that are not routines (data attributes) ---\n')
pprint(inspect.getmembers(inst_B, predicate=lambda x: not inspect.isroutine(x)))

# Code
print('\n--- getsource(ClassB) ---\n')
print(inspect.getsource(ClassB))
print('\n--- getsourcelines(ClassB) ---\n')
pprint(inspect.getsourcelines(ClassB))
