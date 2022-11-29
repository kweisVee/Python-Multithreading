import json
from threading import Thread
import time
import urllib.request

finished_count = 0 

def count_letters(url, frequency):
    response = urllib.request.urlopen(url)
    text = str(response.read())
    for l in text: 
        letter = l.lower()
        if letter in frequency: 
            frequency[letter] += 1
    global finished_count
    finished_count += 1 #increment by one everytimme a thread finishes


def main(): 
    frequency = {}
    for l in "abcdefghijklmnopqrstuvwxyz": 
        frequency[l] = 0

    # use this for the comments: https://www.rfc-editor.org/rfc/rfc1000.txt
    # you can change it to rfc1002 rfc2000 to change the different kinds of documents
    start = time.time()
    for i in range(1000, 1020): 
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)).start()
        time.sleep(0.5)
    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done! Time taken: ", end-start)

main()

# for results between this and the first program didn't match because threads overlap with each other hence 
# not having THREAD SYNCHRONIZATION