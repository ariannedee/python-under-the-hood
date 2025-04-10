"""Show the dunder variables available on functions"""
from a_package.a_module import AClass


def a_function(name: str, shout: bool = False) -> str:
    """Greet someone"""
    greeting: str = "Hello, " + name
    if shout:
        greeting = greeting.upper()
    return greeting


a_function.an_attribute = 'Added to __dict__'


# Top-level function with type annotations
print()
print('a_function dunders')
for dunder in dir(a_function):
    value = getattr(a_function, dunder)
    if not callable(value) and dunder not in '__builtins__':
        print(f'{dunder}: {value}')


# Method in a package module
print()
print('a_method dunders on a class')
for dunder in dir(AClass.a_method):
    value = getattr(AClass.a_method, dunder)
    if not callable(value) and dunder not in ['__builtins__', '__globals__']:
        print(f'{dunder}: {value}')

# Instance method in a package module
print()
print('a_method dunders on an instance')
for dunder in dir(AClass().a_method):
    value = getattr(AClass().a_method, dunder)
    if not callable(value) or dunder in ['__class__', '__func__']:
        print(f'{dunder}: {value}')

# Closures (inner function has access to outer function variables, even after outer function is closed)
a_module_inner = AClass().a_method(1, 2, key_1=3, key_2=4)  # Returns the inner function

print()
print('inner dunders')
print(f'{a_module_inner.__closure__=}')
print(f'{a_module_inner.__name__=}')
print(f'{a_module_inner.__qualname__=}')

a_module_inner()
