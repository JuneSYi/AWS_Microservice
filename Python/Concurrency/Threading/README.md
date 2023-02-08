# Threading
#
- [Creating Threads](#creating-threads)
- [Subclassing Thread](#subclassing-thread)
- [Daemon Thread](#daemon-thread)
- [Lock](#lock)
- [RLock](#rlock)
- [Condition Variables](#condition-variables)
- [Semaphores](#semaphores)
- [Events](#events)
- [Timer](#timer)
- [Barrier](#barrier)
- [With](#with)

#### Creating Threads
##### ./basicThread.py
- import Thread
- Thread construct
    - Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
- from basicThread.py, used start() method to start the thread
- if you use the script in debug mode, you'll see a MainThread and demoThread
    - MainThread - the thread from which the python interpreter was started

#### Subclassing Thread
##### ./subclassing.py
- we can create threads by subclassing the Thread class
- important caveats to remember:
    - we can only override the run() method and the constructor of the Thread class
    - Thread.__init__() must be invoked if the subclass chososes to override the constructor
    - the args or kwargs don't get passed to the run method
- from the output we'll see "subclassThread is executing" followed by "MainThread exiting"

#### Daemon Thread
##### ./daemonExample.py
- daemon is a computer program that runs as a background process; similarily, a daemon thread in python runs in the background
- a python program will not exit until all regular/user threads terminate, a program may exit if the daemon thread is still not finished
- daemon threads exit as soon as the main program thread exits
- can be utilized by marking daemon=True in the Thread class's constructor
    - daemonThread = Thread(target=daemon_thread_task, daemon=True)
- in daemonExample.py, if daemon=False, the main thread exits but the program continues to run...eventually timing out
    - but since we have daemon=True, the main thread exits along with the python program
    - if daemon isn't specified, default is True
- because daemon threads are designe to run in the background, providing services to other non-daemon threads, and they are automatically terminated when there are no more non-daemon threads running, resources such as open files and db connections may not shut-down properly.
    - in these cases, daemon threads are not a good choice for such tasks; may result in improper shutdown and resource leaks

#### Lock
##### ./lockExample.py
- Lock offers two methods:
    - acquire()
    - release()
- a Lock object can only be in two states: locked or unlocked--a Lock object can only be unlocked by a thread that locked it in the first place
- a Lock object is equivalent of a mutex
- acquire()
    - whenever a Lock object is created, any thread can invoke acquire() on the Lock object to lock it (can only be invoked by a single thread due to GIL; other programming languages do not face this limitation)
    - if another thread attempts to acquire(), the thread will be locked until the Lock object is released; if the caller doesn't want to be blocked indefinitely, a floating point timeout value can be passed in the acquire() method.
    - method returns true if the lock is successfully acquired and false if not
- release()
    - changes the state of the Lock object to unlocked
- in lockExample.py we can see the correct usage of acquire() and release() to allow unlocking so that thread2 can begin. you can see from the output that thread2 won't acquire the lock until thread 1 is released.

#### RLock
##### ./rlockExample.py
- a reentrant lock is a lock which can be reacquired by the same thread
- An RLock object carries the notion of ownership; if a thread acquires an RLlock object, it can choose to reacquire it as many times as possible
- in rlockExample.py, if line 20 rlock.release() is commented, the threads attempting to acquire the lock get blocked until it is released
    - the nested acquire/release calls are tracked internally by recursion level; when the recursion level is zero, the reentrant lock is in unlocked state

#### Condition Variables
##### ./conditionVarExamples.py
- condition variables provide mutual exclusion and the ability for threads to wait for a predicate to become true
- two important methods of a condition variable:
    - wait() - invoked to make a thread sleep and give up resources
    - notify() - invoked by a thread when a condition becomes true and the invoking threads want to inform the waiting thead or threads to proceed
- a condition variable is always associated with a lock; the lock can be either reentrant or a plain lock
    - the associated lock must be acquired before a thread can invoke wait() or notify() on the condition variable
- Referring to the two examples in conditionVarExamples.py, we can create a lock ourselves and pass it to the condition variable's constructor. If no lock object is passed then a lock is created underneath the hood by the condition variable.
- when a thread invokes wait(), it simultaneously gives up the lock associated with the condition variable. Only when the sleeping thread wakes up again on a notify(), will it reacquire the lock
- the third example in conditionVarExamples.py shows the idiomatic use of wait()

