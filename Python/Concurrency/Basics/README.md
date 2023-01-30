# Basics
#
- [Program vs Process vs Thread](#program-vs-trocess-vs-thread)
- Concurrency vs Parallism
- Cooperative vs Preemptive Multitasking
- Throughput vs Latency
- Synchronous vs Asynchronous
- I/O Bound vs CPU Bound
- Thread Safety
- Critical Section & Race Conditions
- Deadlock, Liveness & Reentrant Locks
- Mutex vs Semaphore
- Mutex vs Monitor
- Mesa vs Hoare Monitors
- Semaphore vs Monitor
- Global Interpreter Lock
- Amdah's Law
- Moore's Law

#### Introduction
##### ./singleVsMultiThread.py
- we have a single thread doing the summation while in the second scenario, we split the range into two parts and have one thread sum for each range. Once both the threads are complete, we add the two half sums to get the combined sum. Finally, we repeat the previous exercise using processes instead of threads. We measure the time taken for each scenario and print it.
- Data returned:  
System has 16 CPUs  
single threaded took : 2.0878429412841797 seconds and summed to 450000015000000  
multiple threads took : 2.1405434608459473 seconds and summed to 450000015000000  
multiple processes took : 2.243283987045288 seconds and summed to 450000015000000  
- Explanation: Although we would expect the multithreaded function to perform better than single since two threads can work in parallel if the system has at least two CPUs, the relatively poor performance in comparison can be explained by the Global Interpreter Lock (GIL)
    - GIL - an entity within the python framework that allows a single thread to execute even in the presence of more than one idle CPUs
    - multithreaded scenarios may not experience any performance gains in case of CPU-intensive tasks because threads don't execute in parallel and in fact incur an additional cost of management and coalescing partial results
    - With multiple processes, we can expect each process to be scheduled in a separate CPU and work in parallel. However, there's the additional overhead of creating and tearing down proecsses, which is higher than doing the same for threads. Additionally, we utilize Python's interprocess communication machinery, which uses the proxy-pattern and adds network latency to the multiprocessing scenario.

#### Program vs Process vs Thread
- Program - an executable file or a .py script file. In order ot run a program, the OS's kernel is first asked to create a new process, which is an environment in which a program is executed
- Process - a program in execution; consisted of instructions, user-data, system-data segments, CPU, memory, address-space, disk, network I/O
    - Note: 'program' and 'process' are often used interchangeably, most of the time the intet is to refer to a process
- Thread - smallest unit of execution in a process
- multiprocessing - where multiple processes get scheduled on more than one CPU; usually requires multiples cores. Processes don't share any resources amongst themselves whereas threads of a process can share the resources allocated to that particular process, including memory address space

#### Concurrency vs Parallelism
- Serial Execution - when programs are serially executed, they are scheduled one at a time on the CPU without interruption
- Concurrency - A system capable of runnign several distinct programs or more than one independent unit of the same program in overlapping time intervals
    - a concurrent system can have two programs in progress at the same time where progress doesn't imply execution; one program can be suspended while the other executes.
        - goal is to maximize throughput and minimize latency
        - e.g. browser running on a single core machine has to be responsive to user clicks but also be able to render HTML on screen as quickly as possible
        - e.g. OS running on a single core is concurrent but not parallel; it can only process one task at any given point, but all the tasks being managed by the OS appear to make progress because the OS is designed for concurrency--each task gets a slice of CPU time to execute and move forward
- Parallelism - a parallel system is one which necessarily has the ability to execute multiple programs <u>at the same time</u>; usually int he form of multicore processors

#### Cooperative vs Preemptive Multitasking
- multitasking models that achieve concurrency:
    - preemptive multitasking - the OS preempts a program to allow another waiting task to run on the CPU
        - the OS uses a scheduler to determine which task should be executed next, and a mechanism called preemption to interrupt a running task and switch to another task
        - advtange of preemptive multitasking is that it allows the OS to efficiently manage the resources of the ssytem and ensure that no single task monoplizes the CPU
    - cooperative multitasking - aka non-preemptive multitasking, involves well-behaved programs volutnarily giving up control back to the scheduler so that anothe rprogram can run
        - OS's scheduler has no say in how long a program or thread runs for; program or process voluntarily gives up control
        - advantage is being simpler to implement and less pron to race conditions
        - disadvantage is being less robust, as a single misbehaving task can monopolize the CPU and prevent other tasks from running

#### Throughput vs Latency
- Throughput - defined as the rate of doing work or how much work gets done per unit of time
- Latency - time required to complete a task or produce a result; also referred to as response time
- example scenario: in a program that processes hundreds of files, throughput can be the number of files processed by the program in a minute where latency would be the total time taken to completely process all files

#### Synchronous vs Asynchronous
- Synchronous - line-by-line execution of code; synonymous with serial execution
- Asynchronous - execution that doesn't block when invoking subroutines; parallel programming in which a unit of work runs separately from the main applicaiton thread and notifies the calling thread of its completion
    - async methods can return an entity sometimes called future or promise that is the representation of an in-progress computation; the program can query for the status of the computation via the returned future or promise and retrieve the result once compelted
    - another pattern is to pass a callback function to the asynchronous function call, which is invoked with the results when the asynchronous function is done processing

#### I/O Bound vs CPU Bound
- CPU Bound - programs which are compute-intensive are called CPU bound programs; if a CPU bound program is provided a more powerful CPU, it can potentially complete faster
- I/O Bound - opposite of CPU bound. I/O bound programs spend most of their time waiting for input or output operations to complete while the CPU sits idle; I/O operations can consist of operations that write or read from main memory or network interfaces. Because the CPU and main memory are physicall separate, a data bus exists between the two to transfer bits to and fro

#### Thread Safety
##### ./atomicity.py
- If a class or a program has immutable state then the class is necessarily thread-safe
- The shared stated in an application where the same thread mutates the state using an operation that translates into an atomic bytecode instruction can be safely read by multiple read threaders
- In contrast, a sole writer thread mutating the shared state using several atomic bytecode instructions ins't a thread-safe scenario for read threads
- Atomicity - Looking at ./atomicity.py file, the simple statement of count+=1 isn't atomic; it expands into multiple bytecode instructions
    - When two threads invoke the increment() method, it is possible that the first thread is switched out by the python interpreter just before the third INPLACE_ADD instruction is executed. Now the second thread comes along and executes all the six bytecode instructions in one go. When the first thread is rescheduled by the interpret, it executes the third line but the value the thread holds is stale causing it to incorrectly update the count variable.
##### ./threadUnsafeClass.py
- example of an unsafe class where the 'increment()' method modifies the shared 'self.count' variable without any synchronization mechanism to protect against concurent access. As a result, multiple threads may read and write to this variable at the same time, leading to unexpected results.
##### ./threadSafeClass.py
- thread safe version of previous program
- This code uses a lock to fix the thread safety issue. The lock is acquired before the count is incremented, and then released after the increment is done. This ensures that only one thread can execute that section of code at a time, so each increment of the count is atomic and no thread will read an inconsistent value. This way, it ensures that the final count is 500000, instead of an inconsistent value.

#### Critical Section & Race Conditions
- Critical Section - any piece of code that has the possibility of being executed concurrently by more than one thread and exposes any shared data or resources used by the application for access
- Race Condition - when threads run through critical sections without thread synchronization; threads access shared resources or program variables that might be worked on by other threads at the same time causing the data to be inconsistent

#### Deadlock, Liveness & Reentrant
- The following refer to logical follies committed in multithreaded code
- Deadlock - when two or more threads aren't able to make any progress beacuse the rsource required by the first thread is held by the second and the resource required by the second thread is held by the first
- Liveness - ability of a program to execute in a timely manner; if a program experiences a deadlock then it's not exhibiting liveness
- Live-lock - when 2 threads continuously react in response to the actions by the other thread without making any real progress
- Starvation - a thread can experience starvation when it never gets CPU time or access to shared resources
- Reetrant Lock - aka recursive lock, allows for re-locking or re-entering of a sychronization lock
    - if a thread holds a reentrant lock and tries to acquire it again, it will succeed, rather than waiting for the lock to be released by another thread
    - RLock() - type of lock that allows the same thread to acquire the lock multiple times; keeps track of the # of times the lock has been acquired, and releases the lock only when the same thread has released it the same number of times
    ##### ./rLock.py
    - example where rLock() allows reentry by a thread already holding hte lock
    ##### ./threadSafeClass.py
    - In the example of threadSafeClass.py, we can see that the class Counter is using a reentrant lock, which is implemented by the Lock() class from the threading module. The acquire() method is used to acquire the lock, and the release() method is used to release the lock. This ensures that only one thread can execute the increment() method at a time, thus avoiding race conditions and making the code thread-safe.

#### Mutex vs Semaphore
- Mutex - implies mutual exclusion, used to guard shared data such as a linked-list, array, or any primitive type; a mutex allows only a single thread to access a resource or critical section. Once a thread acquires a mutex, all other threads attempting to acquire the same mutex are blocked until teh first thread releases the mutex.
- Sempahore - used for limiting acess to a collection of resources; can also be used for signaling among threads
    - A semaphore with a single permit is called a binary semaphore
    - signaling among threads is an important distinction as it allows threads to cooperatively work towards compelting a task whereas a mutex, is strictly limited to serializing access to shared state among competing threads
- most important difference between the two is that in case of a mutex the same thread must call acquire and subsequent release on the mutex whereas in case of a binary semaphore, different threads can call acquire and release on the semaphore
- a mutex is owned by the thread acquiring it till the point the owning-thread releases it, whereas for a semaphore there's no notion of ownership.

#### Mutex vs Monitor
- a monitor is a mutex plus more
- in a multi-threaded application, a thread needs to wait for some program predicate to be true before it can proceed forward
- Condition Variables
    - There are occasions where spin waiting is used to have a thread repeatedly check if a lock is available. If not available, the thread 'spins' by repeatedly checking the lock's status, rather than blocking the execution of the thread; this can lead to unecessary use of CPU resources if lock is held for an extended amt of time
    - A condition variable is a synchonization primitive that allows a thread to wait for a particular condition to be met. When a thread wants to wait for a condition to be met, it first acquires the associated mutex, then waits on the condition variable. When another thread wants to signal that the condition has been met, it also acuires the mutex, then signals the condition variable. The waiting thread is then woken up and can continue execution.
    - wait() - a method, when called on the condition variable, will cause the associated mutex to be atomically released and the calling thread would be placed in a wait queue.
    - signal() - when the condition variable has been met, signal() is invoked; signal method causes one of the threads that has been placed in the wait queue to get ready for execution (note: only executes after the thread calling the signal() method releases the associated mutex)
- Monitor - made up of a mutex and one or more condition variables
    - can have multiple condition variables
    - a synchronization construct that allows multiple threads to have access to shared data while ensuring that access is mutually exclusive; it provides a way for threads to request and release exclusive access to a shared resource, and also includes mechanisms for signaling other threads that a shared resource has changed.
    - contains a wait set and an entry set
        - wait set - keeps track of the threads that are waiting for a certain condition to be met
        - entry set - keeps track of the threads that are currently executing within the monitor
    - you can think of a monitor as a <u>mutext with a wait set</u>

#### Mesa vs Hoare Monitors
- Mesa Monitors - type of monitor that is implemented using only semaphores; allows only one thread at a time to execute teh critical section of the code and also provides a way for threads to wait for a specific condition to be met before proceeding
    - typically implemented using the 'wait' and 'signal' semaphore operations
- Hoare Monitors - where the signaling thread yields the monitor to the woken up thread, that woken up thread enters the monitor while the original signaling thread sits out. This guarantees that the predicate will not have chagned and instead of checking for the predicate in a while loop, an if-clause would suffice

#### Semaphore vs Monitor
- A monitor is a synchronization object that contains a set of procedures and variables that can be accessed by multiple threads. A monitor provides mutual exclusion to its critical section, meaning that only one thread can execute the critical section at a time. Monitors also include a wait and signal mechanism, which allows threads to wait for a certain condition to be true before proceeding.

- A semaphore, on the other hand, is a simpler synchronization object that only consists of a counter and a set of wait and signal operations. A semaphore is used to control access to a shared resource, and threads can use the wait and signal operations to acquire and release the resource, respectively.

- In general, monitors provide more advanced synchronization features than semaphores, but semaphores are often more lightweight and efficient

#### Global Interpreter Lock
- Python Interpreter - can only execute a single thread at a time; this is the weakness of the reference implementation of Python - CPython
    - Reason: Due to how memory management works in Python
    - The GIL was implemented because the CPython interpreter is not thread-safe. It is written in C and uses a lot of C libraries which are not thread-safe. The GIL is used to prevent conflicts and race conditions that could be caused by multiple threads accessing the interpreter and its data structures simultaneously.
- Summary - Execution of Python bytecode requires acquiring the GIL. This approach prevents deadlocks as there's a single global lock to manage and introduces little overhead. However, the cost is paid by making CPU-bound tasks essentially single-threaded.
- More on the GIL (original source): https://github.com/python/cpython/blob/3.7/Python/ceval_gil.h

#### Amdah's Law
- The law specifies the cap on the max speedup that can be achieved when parallelizing the execution of a program

#### Moore's Law
- states that the number of transistors per square inch on a chip will double every two years
- exponential growth by Moore’s law came to an end more than a decade ago with respect to clock speeds.
