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


print(f"""{Class1.__name__=}
{Class1.__module__=}
{Class1.__doc__=}
{Class1.__annotations__=}
{Class1.__type_params__=}
{Class1.__dict__=}
{Class1.__bases__=}
{Class1.__mro__=}
""")

print(f"""{Class2.__name__=}
{Class2.__module__=}
{Class2.__doc__=}
{Class2.__annotations__=}
{Class2.__type_params__=}
{Class2.__dict__=}
{Class2.__bases__=}
{Class2.__mro__=}
""")

instance_1 = Class1(1)
instance_2 = Class2(2)

print(f"""{instance_1.__module__=}
{instance_1.__doc__=}
{instance_1.__annotations__=}
{instance_1.__dict__=}
{instance_1.__class__=}
""")

print(f"""{instance_2.__module__=}
{instance_2.__doc__=}
{instance_2.__annotations__=}
{instance_2.__dict__=}
{instance_2.__class__=}
""")
