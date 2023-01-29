# Map, Filter, and Reduce are paradigms of functional programming. 
# They allow the programmer (you) to write simpler, shorter code, 
# without neccessarily needing to bother about intricacies like loops and branching.

# Essentially, these three functions allow you to apply a function across a number of iterables, 
# in one fell swoop. map and filter come built-in with Python (in the __builtins__ module) 
# and require no importing. reduce, however, needs to be imported as it resides in the functools module.

# Map
'''
The map() function in python has the following syntax:

map(func, *iterables)

Where func is the function on which each element in iterables (as many as they are) would be applied on. 
Notice the asterisk(*) on iterables? It means there can be as many iterables as possible, 
in so far func has that exact number as required input arguments.
'''
my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)
print("my_pets: ", my_pets)
print(type(my_pets))
print("uppered_pets: ", uppered_pets)
# output: ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']
print(type(uppered_pets))

# example 1 with map()
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)

# example 2 with map()
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.0345341344, 32.000453413]

result = list(map(round, circle_areas, range(1,7)))

print(result)

'''
The zip() function is a function that takes a number of iterables and then creates 
a tuple containing each of the elements in the iterables. Like map(), in Python 3, 
it returns a generator object, which can be easily converted to a list by calling 
the built-in list function on it.
'''
# example with zip()
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers))

print(results)

# Filter
'''
While map() passes each element in the iterable through a function and returns the result 
of all elements having passed through the function, filter(), first of all, requires the 
function to return boolean values (true or false) and then passes each element in the 
iterable through the function, "filtering" away those that are false. It has the following syntax:

filter(func, iterable)

The following points are to be noted regarding filter():

1. Unlike map(), only one iterable is required.

2. The func argument is required to return a boolean type. 
If it doesn't, filter simply returns the iterable passed to it. 
Also, as only one iterable is required, it's implicit that func 
must only take one argument.

3. filter passes each element in the iterable through func and 
returns only the ones that evaluate to true. I mean, it's 
right there in the name -- a "filter".
'''
# Example using filter()
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)
# output: [90, 76, 88, 81]

# Example 2 using filter()
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)
# output: ['madam', 'anutforajaroftuna']

# Reduce
'''
reduce applies a function of two arguments cumulatively to the elements of an iterable, 
optionally starting with an initial argument. It has the following syntax:

reduce(func, iterable[, initial])

Where func is the function on which each element in the iterable gets cumulatively 
applied to, and initial is the optional value that gets placed before the elements 
of the iterable in the calculation, and serves as a default when the iterable is empty. 
The following should be noted about reduce(): 

1. func requires two arguments, 
the first of which is the first element in iterable (if initial is not supplied) and 
the second element in iterable. If initial is supplied, then it becomes the first argument 
to func and the first element in iterable becomes the second element. 

2. reduce "reduces" (I know, forgive me) iterable into a single value.
'''
from functools import reduce

numbers = [3, 4, 6]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)
# output: 13

result = reduce(custom_sum, numbers, 7)
print(result)
# output: 20
