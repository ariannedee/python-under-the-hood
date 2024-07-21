"""Altering immutable variables means pointing to a new object at a new location.
In CPython, the id is an int representing the memory location of an object."""


def print_id(obj):
    print(f"""ID of {obj}:
    {id(obj)}
    {hex(id(obj))}
    {super(type(obj), obj).__repr__()}
    """)


# These are the same because they refer to the same object
x = 256
y = x
print_id(x)
print_id(y)

# These are different because x refers to a new object
# Same if object is interred or immortal (-5 <= x <= 255)
x += 1
print_id(x)
print_id(y)

# These may or may not be the same depending on the initial value of x
y += 1
print_id(x)
print_id(y)
