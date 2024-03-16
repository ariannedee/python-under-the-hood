"""Show the dunder variables available on custom classes"""


class Class1:
    """Class 1 docs"""
    class_attr_1: str = '1'

    def __init__(self, param: int):
        self.inst_attr_1: int = param


class Class2(Class1):
    class_attr_2: list = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inst_attr_2: dict = {}

    @property
    def property_2(self):
        return 2


print()
print('Class1 attributes')
for dunder in dir(Class1):
    value = getattr(Class1, dunder)
    if not callable(value):
        print(f'{dunder}: {value}')

print()
print('Class2 attributes')
for dunder in dir(Class2):
    value = getattr(Class2, dunder)
    if not callable(value):
        print(f'{dunder}: {value}')


instance_1 = Class1(1)
instance_2 = Class2(2)

print()
print('instance_1 attributes')
for dunder in dir(instance_1):
    value = getattr(instance_1, dunder)
    if not callable(value) or dunder == '__class__':
        print(f'{dunder}: {value}')

print()
print('instance_2 attributes')
for dunder in dir(instance_2):
    value = getattr(instance_2, dunder)
    if not callable(value) or dunder == '__class__':
        print(f'{dunder}: {value}')
