"""
This program creates one list and one set from all the words in the file "words.txt"
then search for a specific words for 1000 times in each of them and print the time
it took to conduct each search.
"""

import time


def create_list():
    # returns a list from all the words in the file 'words.txt'
    file = open('words.txt', 'r')
    return list(file.read().split())


def create_set():
    # returns a set from all the words in the file 'words.txt'
    return set(create_list())


def average_runtime():
    # prints the average time took to conduct a search 1000 times in list vs in a set.

    words_list = create_list()
    words_set = create_set()

    start_time = time.time()
    for x in range(1000):
        if 'zwitterion' in words_list:
            pass
    end_time = time.time()
    print(f'running search in words_list took {(end_time - start_time) / 1000} ')

    start_time = time.time()
    for y in range(1000):
        if 'zwitterion' in words_set:
            pass
    end_time = time.time()
    print(f'running search in words_list took {(end_time - start_time) / 1000} ')


average_runtime()
