class WithoutSlots:
    def __init__(self):
        self.attr_1 = 1
        self.attr_2 = 2


class WithSlots:
    __slots__ = ('attr_1', 'attr_2')

    def __init__(self):
        self.attr_1 = 1
        self.attr_2 = 2


without_slots = WithoutSlots()
without_slots.attr_3 = 3
print(without_slots.__dict__)

with_slots = WithSlots()
try:
    with_slots.attr_3 = 'Error'
except AttributeError as e:
    print('\nTrying to set an attribute not in slots:')
    print(repr(e))

try:
    print(with_slots.__dict__)
except AttributeError as e:
    print('\nTrying to access __dict__ when __slots__ is set:')
    print(repr(e))
    tb = e.__traceback__
    print(tb.tb_frame)
