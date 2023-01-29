import random

def lottery():
    # returns 6 numbers between 20 and 40
    for i in range(6):
        # yield suspends a function's exeuction and sends a value back to the caller, but retains enough state to enable
        # the function to resume where it left off. When the function resumes, it continues execution immediately after the last yield run.
        # This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list
        yield random.randint(20, 40)

    # returns a 7th number between 1 and 20
    yield random.randint(1, 20)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))
       
'''
The function lottery() uses the yield statement to generate a series of random numbers. 
The yield statement suspends the execution of the function, sends a value back to the caller, 
but retains enough state to enable the function to resume where it left off. 
The for loop iterates over the values generated by the function, 
and the print statement displays each value as it is generated.

When the function is first called, it runs until it reaches the first yield statement, 
at which point it returns a random number between 20 and 40. 
When the next value is requested, the function resumes execution immediately after the last yield statement, 
generating another random number between 20 and 40. This process is repeated until the function has generated 6 random numbers between 20 and 40.

After the 6th random number is generated, the function continues execution and the next yield statement is reached which yields a 7th random number between 1 and 20.

This allows the function's code to produce a series of values over time, rather than computing them all at once and returning them as a list.
'''