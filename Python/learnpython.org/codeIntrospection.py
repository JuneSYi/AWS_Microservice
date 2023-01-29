# Code introspection is the ability to examine classes, 
# functions and keywords to know what they are, what they do and what they know.

'''
help()
dir() 
hasattr() 
id() 
type() 
repr() 
callable() 
issubclass() 
isinstance() 
__doc__ 
__name__
'''
# Use the help function to see what each function does
# help(dir)
'''
Help on built-in function dir in module builtins:
    
    dir(...)
        dir([object]) -> list of strings
        
        If called without an argument, return the names in the current scope.
        Else, return an alphabetized list of names comprising (some of) the attributes
        of the given object, and of attributes reachable from it.
        If the object supplies a method named __dir__, it will be used; otherwise
        the default dir() logic is used and returns:
          for a module object: the module's attributes.
          for a class object:  its attributes, and recursively the attributes
            of its bases.
          for any other object: its attributes, its class's attributes, and
            recursively the attributes of its class's base classes.
'''
# help(hasattr)
'''
Help on built-in function hasattr in module builtins:
    
    hasattr(obj, name, /)
        Return whether the object has an attribute with the given name.
        
        This is done by calling getattr(obj, name) and catching AttributeError.
'''
# help(id)
'''
Help on built-in function id in module builtins:
    
    id(obj, /)
        Return the identity of an object.
        
        This is guaranteed to be unique among simultaneously existing objects.
        (CPython uses the object's memory address.)
'''

# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
print(dir(Vehicle))
'''
 ['__class__', '__delattr__', '__dict__', '__dir__', 
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
 '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', 
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
 '__weakref__', 'color', 'description', 'kind', 'name', 'value']
 '''