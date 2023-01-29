# Basics

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
Program - an executable file or a .py script file. In order ot run a program, the OS's kernel is first asked to create a new process, which is an environment in which a program is executed  
Process - a program in execution; consisted of instructions, user-data, system-data segments, CPU, memory, address-space, disk, network I/O  
    - Note: 'program' and 'process' are often used interchangeably, most of the time the intet is to refer to a process
Thread - smallest unit of execution in a process  
multiprocessing - where multiple processes get scheduled on more than one CPU; usually requires multiples cores. Processes don't share any resources amongst themselves whereas threads of a process can share the resources allocated to that particular process, including memory address space

#### Concurrency vs Parallelism
- Serial Execution - when programs are serially executed, they are scheduled one at a time on the CPU without interruption
- Concurrency - A system capable of runnign several distinct programs or more than one independent unit of the same program in overlapping time intervals
    - a concurrent system can have two programs in progress at the same time where progress doesn't imply execution; one program can be suspended while the other executes.
        - goal is to maximize throughput and minimize latency
        - e.g. browser running on a single core machine has to be responsive to user clicks but also be able to render HTML on screen as quickly as possible
        - e.g. OS running on a single core is concurrent but not parallel; it can only process one task at any given point, but all the tasks being managed by the OS appear to make progress because the OS is designed for concurrency--each task gets a slice of CPU time to execute and move forward
- Parallelism - a parallel system is one which necessarily has the ability to execute multiple programs <u>at the same time</u>; usually int he form of multicore processors

#### Cooperative vs Preemptive Multitasking
