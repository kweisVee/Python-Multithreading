import json
from threading import Thread, Lock
import time
import urllib.request

finished_count = 0 

def count_letters(url, frequency, mutex):
    response = urllib.request.urlopen(url)
    text = str(response.read())
    mutex.acquire()
    for l in text: 
        letter = l.lower()
        if letter in frequency: 
            frequency[letter] += 1 #if we call the mutex for every letter, it will be smaller
    
    global finished_count
    finished_count += 1 #increment by one everytimme a thread finishes
    #mutex should be placed after finished_count as it is also shared in between threads
    mutex.release()


def main(): 
    frequency = {}
    mutex = Lock()
    for l in "abcdefghijklmnopqrstuvwxyz": 
        frequency[l] = 0

    # use this for the comments: https://www.rfc-editor.org/rfc/rfc1000.txt
    # you can change it to rfc1002 rfc2000 to change the different kinds of documents
    start = time.time()

    for i in range(1000, 1020): 
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex)).start()

    #because we have to check the finished count that is used in other threads, we have to add a mutex here as well  
    while True: 
        mutex.acquire()
        if finished_count == 20: 
            break
        mutex.release()
        time.sleep(0.5)
    #this code below is not allowed since it will be sleeping and it can't realease the mutex lock so we need to change
    #to protect the finished_count variable
    # while finished_count < 20: 
    #     time.sleep(0.5)
    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done! Time taken: ", end-start)

main()

