import json
import time
import urllib.request
from collections import Counter

def count_letters(url, frequency):
    response = urllib.request.urlopen(url)
    text = str(response.read())
    for l in text: 
        letter = l.lower()
        if letter in frequency: 
            frequency[letter] += 1


def main(): 
    frequency = {}
    for l in "abcdefghijklmnopqrstuvwxyz": 
        frequency[l] = 0

    # use this for the comments: https://www.rfc-editor.org/rfc/rfc1000.txt
    # you can change it to rfc1002 rfc2000 to change the different kinds of documents
    start = time.time()
    for i in range(1000, 1020): 
        count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)
    end = time.time()
    print(json.dumps(frequency, indent=4))
    print("Done! Time taken: ", end-start)

main()