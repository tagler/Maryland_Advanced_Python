from functools import wraps
import time

# Decorator that times a function. 
def timer(func):
    # start timer
    start_time = time.time()
    # inner function 
    @wraps(func)
    def inner(*args):
        func(*args)
    # end timer
    return time.time() - start_time

# Function that adds 1 to input, decorator returns execution time. 
@timer
def add_one(x):
    return x+1

# Tests decorator.
print(add_one)
