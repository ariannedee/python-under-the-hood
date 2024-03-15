class MyClassDescriptor:
    def __init__(self):
        self.value = 10

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class MyInstanceDescriptor:
    def __init__(self):
        self.value = {}

    def __get__(self, instance, owner):
        obj = instance if instance else owner
        return self.value.get(obj, None)

    def __set__(self, instance, value):
        self.value[instance] = value


class AClass:
    a = MyClassDescriptor()
    b = MyInstanceDescriptor()


if __name__ == '__main__':
    obj = AClass()
    print("Class descriptor\n")
    print(f"{AClass.a=}")
    print(f"{obj.a=}")
    obj.a = 20
    print(f"{AClass.a=}")
    print(f"{obj.a=}")

    print("\nInstance descriptor\n")
    print(f"{AClass.b=}")
    print(f"{obj.b=}")
    AClass.b = 1
    obj.b = 2
    print(f"{AClass.b=}")
    print(f"{obj.b=}")
