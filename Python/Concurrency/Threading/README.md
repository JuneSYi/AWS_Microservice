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