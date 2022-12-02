from asyncio import Lock
import os
from os.path import join, isdir
from threading import Thread

mutex = Lock()

matches = []

def file_search(root, filename): 
    print(f"Searching in: {root}")

    child_threads = []

    # os.listdir lists all the files in that directory
    for file in os.listdir(root):
        full_path = join(root, file) #concatinates the root and the file
        if filename in file: 
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path): 
            # we have to do this since it's recursive
            t = Thread(target=file_search, args=([full_path, filename]))
            t.start()
            # can't do t.join or else we have to wait for each thread to complete its search which makes it not parallel
            child_threads.append(t)
    for t in child_threads: 
        t.join()

def main(): 
    t = Thread(target=file_search, args=([os.path.expanduser('~/Desktop'), "README.md"]))
    t.start()
    t.join()
    for m in matches: 
        print(f"matched: {m}")

main()