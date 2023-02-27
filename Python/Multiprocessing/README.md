# Multiprocessing
#

#### Introduction
- Most of the APIs in the module mirror the APIs found in the threading module
- The multiprocessing module offers hope by allowing a program to spin-off tasks as separate processes that can then run on individual processors. This allows Python to be both concurrent and parallel, whereas with the threading module, Python is only concurrent and not parallel.

#### Process
- Process()
    - The constructor of the Process class accepts a callable object that the spawned process then executes.

#### Fork
- process for unix based systems

#### Spawn
- Spawn is essentially a combination of fork followed by an exec (one of its variants) system call. Depending on the platform, posix_spawn system call may also be used. posix_spawn is roughly a combination of fork and exec with some optional housekeeping steps between the two calls.
- This solves the problem we encountered with fork start method. The module state isn’t inherited by a child process, rather it starts from scratch. A new python interpreter process is created and the child doesn't inherit any resources from the parent process other than those required to execute the specified callable target.
- Exec system call
    - In order to understand spawn, we'll examine the exec family of system calls. When you issue an ls or a find command in your terminal, the shell first forks itself and then invokes one of the variants of the exec family of system calls. Briefly, an exec call transforms the calling process into another. The program in the calling process is replaced with another program and is run from the entry point. Realize the distinction between a program and a process as it matters in this context. The program is just a set of instructions and data that is used to initialize a process. Using exec, the running process loads a program (instructions and data) and replaces its own program with the loaded one and starts execution.
    - Both fork and exec can be called independently and need not be called in succession. For instance, a process that is ending can simply call exec and start another program rather than forking itself. Similarly, a process listening on a socket may want to fork itself to let the child process deal with a received request while it goes back to listening. But the usual way to create a new process in the Unix world is to first fork in the parent process and then exec in the child process. The child process's PID doesn't change and the parent process can wait for the child process to finish before resuming execution.
    - Remember, forking produces two processes, whereas exec loads an executable in the existing process's address space. The current executable image is replaced with another one loaded from an executable file.

#### Forkserver
- With forkserver as the start method, a brand new single-threaded process, called server is started. Whenever, a new process needs to be created, the parent process connects to the server and requests that it forks a new process. Since the server process is single threaded, it can safely invoke os.fork() to create a new process.

#### Queues & Pipes
-








#### ./lambdaParallelExecution.py
##### Pulled from https://aws.amazon.com/blogs/compute/parallel-processing-in-python-with-aws-lambda/
- Due to the Lambda execution environment not having /dev/shm (shared memory for processes) support, you can’t use multiprocessing.Queue or multiprocessing.Pool.
- On the other hand, you can use multiprocessing.Pipe
