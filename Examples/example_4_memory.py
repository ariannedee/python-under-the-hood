"""
Each function call creates a new layer on the call stack. Local variables live here.
The value of the variables (objects) are stored in the heap.

Once a function returns, its layer on the stack is removed and its memory is freed.
Once the number of references to a heap object drops to 0, the memory is freed.
"""


def func_2(x):
    x = x - 1
    return x


def func_1(x):
    x = x * 2
    y = func_2(x)
    return y


x = 2
y = func_1(x)
