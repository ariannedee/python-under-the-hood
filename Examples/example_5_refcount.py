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
