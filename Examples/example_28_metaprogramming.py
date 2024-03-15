"""Custom SimpleEnum implementation

Enum members have a name and value.
Enums can be iterated over.
"""
import re


class EnumMemberMeta(type):
    """Defines how the Enum members get printed"""
    def __new__(cls, name, bases, attrs):
        obj = super().__new__(cls, name, bases, attrs)
        obj.enum_name = name
        obj.name = attrs.get('name', '')
        obj.value = attrs.get('value', '')
        return obj

    def __str__(self):
        return f"{self.enum_name}.{self.name}"

    def __repr__(self):
        return f"<{self.enum_name}.{self.name}: {self.value}>"


def create_enum_member(enum_name, member_name, value):
    """Creates an enum member with a name and value"""
    new_class_attrs = {
        'name': member_name,
        'value': value,
        '__annotations__': {'name': str},
    }
    return EnumMemberMeta(enum_name, (), new_class_attrs)


class EnumMeta(type):
    def __new__(cls, name, bases, attrs):
        def is_dunder(name_): return re.fullmatch(r'__\w+__', name_)

        # Gather all user-defined class attributes
        class_attrs = {}
        non_class_attrs = {}
        for attr_name, attr_value in attrs.items():
            if is_dunder(attr_name):
                non_class_attrs[attr_name] = attr_value
            else:
                class_attrs[attr_name] = attr_value

        # Turn class attrs into enum members
        enum_attrs = {}
        for attr_name, attr_value in class_attrs.items():
            member = create_enum_member(name, attr_name, attr_value)
            enum_attrs[attr_name] = member

        # Create new namespace __dict__
        all_attrs = non_class_attrs
        all_attrs.update(enum_attrs)
        all_attrs['enum_attrs'] = enum_attrs

        return super().__new__(cls, name, bases, all_attrs)

    def __iter__(self):
        for member in self.enum_attrs.values():
            yield member


class SimpleEnum(metaclass=EnumMeta):
    """All implementation is in EnumMeta.
    Can create new class with:
        1. class EnumName(SimpleEnum):
               ...
        2. class EnumName(metaclass=EnumMeta):
               ...
    """
    pass


class Rating(SimpleEnum):
    good = 1
    okay = 0
    bad = -1


print(Rating.good)               # Rating.good
print(repr(Rating.good))         # <Rating.good: 1>
print(Rating.good.name.upper())  # good
print(Rating.good.value)         # 1

for rating in Rating:
    print(repr(rating))
