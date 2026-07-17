#with threads
#thread: Threads allow multiple tasks to run concurrently within the same program.
#A thread is a lightweight unit of execution inside a process.

from threading import *
import time

def task1():
    for i in range(3):
        print("Task 1")
        time.sleep(1)

def task2():
    for i in range(3):
        print("Task 2")
        time.sleep(1)

t1 = Thread(target=task1)
t2 = Thread(target=task2)

t1.start()
t2.start()