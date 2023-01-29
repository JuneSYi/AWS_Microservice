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