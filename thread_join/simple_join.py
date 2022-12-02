# CHILD AND PARENT THREAD
from threading import Thread
import time


def child(): 
    print("Child thread doing work")
    time.sleep(5)
    print("Child thread done")

def parent(): 
    t = Thread(target=child, args=())
    t.start()
    print("Parent thread is waiting...")
    t.join() #this waits until the child thread is finished
    print("Parent thread is unblocked...")

parent()