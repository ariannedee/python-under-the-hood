"""Some documentation for this module"""
from pprint import pprint

import hello
from a_package import a_module

my_str: str = 'abc'


print()
print("This module's variables:")
pprint(vars())

print()
print("hello's variables:")
pprint(vars(hello))

print()
print("a_package.a_module's variables:")
pprint(vars(a_module))
