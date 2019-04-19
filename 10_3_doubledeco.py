from functools import wraps

# Decorator that doubles value of function.
def double(func):
    @wraps(func)
    def inner(*args):
        return func(*args) + func(*args)
    return inner

# Function that adds 1 to input.
def add_one(x):
    return x + 1

# Function that adds 1 to input and then doubles using decorator. 
@double
def add_one_double(x):
    return x + 1

# Function that barks once.
def bark():
    return "woof! "

# Function that barks once and then dobules using decorator.
@double
def bark_double():
    return "woof! "

# Tests Decorator. 
print(add_one(1), add_one_double(1))
print(add_one(2), add_one_double(2))
print(add_one(3), add_one_double(3))
print(bark(), bark_double())

