# A decorator is a design pattern in Python that allows a user to add new functionality 
# to an existing object without modifying its structure. 
# Decorators are usually called before the definition of a function you want to decorate. 

# Functions can also be passed as parameters to other functions.
def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)
# output: 6

# A function can also generate another function
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
hello()
# output: 'Hi'

# a simple decorator that will convert a sentence to uppercase. We do this by defining a wrapper inside an enclosed function.
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
'''
Our decorator function takes a function as an argument, and we shall, therefore, define a function and pass it to our decorator.
'''
def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
decorate()
# output: 'HELLO THERE'

# Python provides a much easier way for us to apply decorators using @
print("using @uppercase_decorator to capitalize 'hello there'")
@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi()
print(say_hi())
#output: 'HELLO THERE'