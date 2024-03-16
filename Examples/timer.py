import time


def timeit(func):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.perf_counter()
            print(f"Function {func.__name__} took {end - start}s")
    return inner
