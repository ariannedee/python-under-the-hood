"""Copying mutable variables.
Shows variable reassignment, shallow copy and deep copy."""
import copy

a = [[]]
b = a                 # References same object as a
c = copy.copy(a)      # Shallow copy - id(c) != id(a) but contents are the same objects
d = copy.deepcopy(a)  # Deep copy - all contents are new objects

a.append(1)
a[0].append(2)
print(a)  # [[2], 1]
print(b)  # [[2], 1]
print(c)  # [[2]]
print(d)  # [[]]
