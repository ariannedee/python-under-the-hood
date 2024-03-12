"""Check reference count on objects that have been deleted"""
import ctypes


# this class will allow us to access the object from memory (even after it is deleted)
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]


my_dict_1 = {}
my_dict_2 = {}

# Create cyclical reference
my_dict_1['dict2'] = my_dict_2
my_dict_2['dict1'] = my_dict_1

obj_address = id(my_dict_1)  # get memory address of my_dict_1

print(PyObject.from_address(obj_address).refcnt)  # my_dict_1 has 2 references

del my_dict_1, my_dict_2  # deleting both objects
print(PyObject.from_address(obj_address).refcnt)  # my_dict_1 has 1 reference still
