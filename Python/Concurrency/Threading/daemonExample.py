from threading import Thread
from threading import current_thread
import time

def daemon_thread_task():
    while True:
        print("{0} executing".format(current_thread().getName()))
        time.sleep(1)

regularThread = Thread(target=daemon_thread_task, name="daemonThread", daemon=True)
regularThread.start()  # start the daemon thread

time.sleep(3)

print("Main thread exiting and Python program too")