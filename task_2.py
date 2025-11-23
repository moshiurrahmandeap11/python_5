# Decorators

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start:.4f} seconds")
        return result
    return wrapper


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

# Example usage:
@timing_decorator
@log_decorator

def add(a, b):
    time.sleep(1)  # Simulate a time-consuming operation
    return a + b
result = add(5, 10)
print(f"Final Result: {result}")
