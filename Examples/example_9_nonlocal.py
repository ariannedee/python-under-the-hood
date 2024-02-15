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
