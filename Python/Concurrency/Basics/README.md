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