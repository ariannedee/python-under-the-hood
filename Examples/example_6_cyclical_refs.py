import ctypes


# this class will allow us to access the object from memory (even after it is deleted)
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]


my_dict_1 = {}
my_dict_2 = {}

my_dict_1['dict2'] = my_dict_2
my_dict_2['dict1'] = my_dict_1

obj_address = id(my_dict_1)  # getting memory address to track memory block

print(PyObject.from_address(obj_address).refcnt)  # 2 refs to my_dict_1

del my_dict_1, my_dict_2  # deleting both objects
print(PyObject.from_address(obj_address).refcnt)  # 1 ref to my_dict_1 after deleted
