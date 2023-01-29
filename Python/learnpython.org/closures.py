# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    print(number)
    # 9
    printer()
    # 3
    print(number)
    # 3

print_msg(9)
# if we didn't use nonlocal, the second print(number) would output 9

def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()
# outputs: Burn the Sun!
# Even though the execution of the "transmit_to_space()" was completed, the message was rather preserved. 
# This technique by which the data is attached to some code even after end of those other original functions is called as closures in python


# a nested loop and a python closure to make functions to get multiple multiplication functions using closures
def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
# output: 45