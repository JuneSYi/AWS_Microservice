# Multiprocessing
#

#### Introduction
- Most of the APIs in the module mirror the APIs found in the threading module
- The multiprocessing module offers hope by allowing a program to spin-off tasks as separate processes that can then run on individual processors. This allows Python to be both concurrent and parallel, whereas with the threading module, Python is only concurrent and not parallel.

#### Process
- 

#### ./lambdaParallelExecution.py
##### Pulled from https://aws.amazon.com/blogs/compute/parallel-processing-in-python-with-aws-lambda/
- Due to the Lambda execution environment not having /dev/shm (shared memory for processes) support, you can’t use multiprocessing.Queue or multiprocessing.Pool.
- On the other hand, you can use multiprocessing.Pipe
