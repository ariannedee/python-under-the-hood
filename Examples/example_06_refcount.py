"""Check the number of references to an object. Will always be at least 1."""
import sys

a = []
print(sys.getrefcount(a))  # 2

b = a
print(sys.getrefcount(a))  # 3

c = [a]
print(sys.getrefcount(a))  # 4

del b
print(sys.getrefcount(a))  # 3

del a

print(c)
print(sys.getrefcount(c[0]))  # 2
