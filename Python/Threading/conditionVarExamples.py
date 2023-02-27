from threading import Condition

'''
Creating a condition variable by passing a custom lock
'''
lock = Lock()
cond_var = Condition(lock) # pass custom lock to condition variable
cond_var.acquire()
cond_var.wait()

'''
Creating a condition variable without passing a lock
'''
cond_var = Condition()
cond_var.acquire()
cond_var.wait()

'''
idiomatic use of wait()

cond_var.acquire()
while(condition_to_test is not satisfied):
    cond_var.wait()
# condition is now true, perform necessary tasks
cond_var.release()
'''

'''
idiomatic use of notify()

cond_var.acquire()
set condition_to_test to true/satisfied
cond_var.notify()
cond_var.release()
'''