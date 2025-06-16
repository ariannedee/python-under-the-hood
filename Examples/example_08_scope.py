"""Show the variables at different scopes:
- local (in function)
- enclosed (in outer function)
- global
- builtins

Makes use of locals(), globals() and vars() builtin functions
"""
from math import pi as PI
from pprint import pprint

r = -1000


def circumference(r):

    def diameter():
        d = 2 * r

        print('inner:')
        pprint(locals())
        print()

        return d

    area = diameter() * PI

    print('outer:')
    pprint(locals())
    print()

    return area


area_1 = circumference(1)
area_2 = circumference(2)

print('global:')
pprint(globals())
print()

print('builtins:')
pprint(vars(__builtins__))
