"""
This program creates one list and one set from all the words in the file "words.txt"
then search for a specific words for 1000 times in each of them and print the time
it took to conduct each search.
"""

import time


def create_list():
    # returns a list from all the words in the file 'words.txt'
    file = open('words.txt', 'r')
    words_list = list(file.read().split())
    return words_list


def create_set():
    # returns a set from all the words in the gile 'words.txt'
    words_set = set(create_list())
    return words_set


def average_runtime():
    words_list = create_list()
    words_set = create_set()

    start_time = time.time()
    for x in range(1000):
        if 'zwitterion' in words_list:
            pass
        else:
            pass
    end_time = time.time()
    print(f'running search in words_list took {end_time - start_time} ')

    start_time = time.time()
    for x in range(1000):
        if 'zwitterion' in words_set:
            pass
        else:
            pass
    end_time = time.time()
    print(f'running search in words_list took {end_time - start_time} ')


average_runtime()
