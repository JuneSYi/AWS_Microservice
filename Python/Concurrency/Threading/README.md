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