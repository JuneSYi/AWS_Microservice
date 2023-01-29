# It is possible to declare functions which receive a variable number of arguments, using the following syntax:
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("foo And all the rest... %s" % list(therest))
    
def bar(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %((therest,)))
    print(type(therest))
    print(type(list(therest)))

foo(1,2,3,4,5,6)
bar(1, 2, 3, 4, 5)

# It is also possible to send functions arguments by keyword, so that the order of the argument does not matter, 
# using the following syntax. 
# The following code yields the following output: The sum is: 6 Result: 1
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))
'''
The "bar" function receives 3 arguments. If an additional "action" argument is received, 
and it instructs on summing up the numbers, then the sum is printed out. 
Alternatively, the function also knows it must return the first argument, 
if the value of the "number" parameter, passed into the function, is equal to "first".
'''