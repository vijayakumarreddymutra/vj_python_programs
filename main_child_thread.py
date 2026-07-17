#main thread and child thread

#best example for this: if you are playing any game you hear bgm, if you come out the game, bgm will stop

from threading import *
import time

def job():
    while True:
        print("Child Thread job...")
        time.sleep(2)

t = Thread(target=job,daemon=True)
t.start()

print("Main Thread Executing...")
time.sleep(3)
print("Main Thread Finished")