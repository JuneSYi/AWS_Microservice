from threading import Thread
from threading import Condition
import time


def printer_thread_func():
    global prime_holder
    global found_prime

    while not exit_prog:
        # wait for a prime number to become
        # available for printing
        cond_var.acquire()
        '''
        We would want a printer thread to make progress only when the condition 
        found_prime is set to true. This can only be possible with a while loop 
        where we check if the condition found_prime is true before allowing a 
        printer thread to move ahead.
        '''
        while not found_prime and not exit_prog:
            '''
            when a thread invokes wait(), it simultaneously gives up the lock
            associated with the condition variable

            only when the sleeping thread wakes up again on a notify(), 
            will it reacquire the lock
            '''
            
            cond_var.wait()
        cond_var.release()

        if not exit_prog:
            print(prime_holder)
            # reset. We can skip this statement if we like
            prime_holder = None
            # acquire() locks thread
            cond_var.acquire()
            found_prime = False
            # notify() wakes up thread on wait() condition
            cond_var.notify()
            # release() unlocks
            cond_var.release()


def is_prime(num):
    if num == 2 or num == 3:
        return True
    div = 2
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


def finder_thread_func():
    global prime_holder
    global found_prime
    i = 1
    while not exit_prog:
        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so that we can see the output
            time.sleep(.01)
        prime_holder = i
        # once a prime # is found, it uses acquire() to change state to locked
        '''
        A Lock is an object that acts like a hall pass. 
        Only one thread at a time can have the Lock. 
        Any other thread that wants the Lock must wait until the 
        owner of the Lock gives it up.
        '''
        cond_var.acquire()
        found_prime = True
        cond_var.notify()
        cond_var.release()

        cond_var.acquire()
        # waits until found_prime = False and notify() is triggered
        while found_prime and not exit_prog:
            cond_var.wait()
        cond_var.release()
        # changes to next number
        i += 1


cond_var = Condition()
found_prime = False
prime_holder = None
exit_prog = False

printerThread = Thread(target=printer_thread_func)
printerThread.start()

finderThread = Thread(target=finder_thread_func)
finderThread.start()

# Let the threads run for 3 seconds
time.sleep(3)

# Let the threads exit
exit_prog = True
'''
the acquire(), notifyAll(), and release() calls after setting exit_prog to True 
are used to ensure that all waiting threads are notified and released in case any 
of them are blocked on the Condition variable. Without these calls, any waiting 
threads would continue to block indefinitely, even after the exit_prog flag has 
been set to True.
'''
cond_var.acquire()
cond_var.notifyAll()
cond_var.release()

'''
without calling join() on both threads, the main program may still exit before the 
threads have a chance to complete their execution. By calling join(), the main 
program waits for both threads to complete their execution before exiting, which 
ensures that all resources are properly cleaned up and that the program exits gracefully.

So, while the exit_prog flag does cause the threads to terminate their execution, 
calling join() on both threads is still necessary to ensure a clean exit and avoid 
resource leaks.
'''
printerThread.join()
finderThread.join()
