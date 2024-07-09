"""The nonlocal keyword can be used to alter an outer function variable within an inner function
If an outer function goes out of scope, the inner function can still reference it.
"""


def outer(var):
    def inner():
        nonlocal var
        var += 1
        return var

    print(var)
    return inner


closure = outer(5)

print(closure())
print(closure())
print(closure())
print(closure())
