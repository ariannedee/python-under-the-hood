"""The global keyword can be used to alter a global variable within a function"""
num_calls = 0


def a_function():
    global num_calls
    num_calls += 1
    print(f"Function called {num_calls} times")


a_function()
a_function()
a_function()
