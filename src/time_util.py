from functools import wraps
from time import time


# Decorator to time the execution of the given method
def timeit(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = method(*args, **kwargs)
        end_time = time()
        print(f"{method.__name__} => {(end_time - start_time)*1000} ms")

        return result

    return wrapper
