"""The nonlocal keyword can be used to alter an outer function variable within an inner function"""

var = 1


def outer(var):
    def inner():
        nonlocal var
        var = 3

    print(var)  # 2
    inner()
    print(var)  # 3


outer(2)
print(var)  # 1
