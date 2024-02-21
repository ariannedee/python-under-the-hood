from math import pi
from pprint import pprint

r = -1000


def circumference(r):

    def diameter():
        d = 2 * r

        print('inner:')
        pprint(locals())
        print()

        return d

    area = diameter() * pi

    print('outer:')
    pprint(locals())
    print()

    return area


area_1 = circumference(1)
area_2 = circumference(2)

print('global:')
pprint(locals())
print()

print('builtins:')
pprint(vars(__builtins__))
