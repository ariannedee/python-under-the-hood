"""
vars - https://docs.python.org/3/library/functions.html#vars
  vars(): returns locals()
  vars(obj): returns the __dict__ mapping of attributes of an object

dir - https://docs.python.org/3/library/functions.html#dir
  dir(): returns a list of names in the current scope (keys of locals() dict)
  dir(obj): attempts to return a list of valid attributes for the object (i.e. obj.{attr})
"""
import pprint


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
    pprint.pprint(vars())
    print('\nlocal dir()')
    pprint.pprint(dir())


# Locals
a_func(6)

# Globals
print('\nglobal vars()')
pprint.pprint(vars())
print('\nglobal dir()')
pprint.pprint(dir(), compact=True)

# Function
print('\nvars(a_func)')
print(vars(a_func))
print('\nlocal dir(a_func)')
pprint.pprint(dir(a_func), compact=True)

# Module
print('\nvars(pprint)')
print(vars(pprint))
print('\nlocal dir(pprint)')
pprint.pprint(dir(pprint), compact=True)

# Class
print('\nvars(ClassA)')
pprint.pprint(vars(ClassA))
print('\ndir(ClassA)')
pprint.pprint(dir(ClassA), compact=True)
print('\nvars(inst_A)')
pprint.pprint(vars(inst_A))
print('\ndir(inst_A)')
pprint.pprint(dir(inst_A), compact=True)

# Subclass
print('\nvars(ClassB)')
pprint.pprint(vars(ClassB))
print('\ndir(ClassB)')
pprint.pprint(dir(ClassB), compact=True)
print('\nvars(inst_B)')
pprint.pprint(vars(inst_B))
print('\ndir(inst_B)')
pprint.pprint(dir(inst_B), compact=True)

pprint.pprint(vars(ClassB.__init__))