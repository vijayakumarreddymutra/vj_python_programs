#without threads

import time

def task1():
    for i in range(3):
        print("Task 1")
        time.sleep(1)

def task2():
    for i in range(3):
        print("Task 2")
        time.sleep(1)

task1()
task2()