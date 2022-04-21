"""
This Program prints all the perfect numbers from 0 to infinity.
Perfect number is a number that the sum of its divisors is the number itself.
"""

import math

def check_divisors():
    # generates all the divisors of a number

    current_num = 1
    sum_divisors = 0
    while True:
        for i in range(1, math.sqrt(current_num)):
            if current_num % i == 0:
                sum_divisors += i
        if sum_divisors == current_num:
            yield current_num
        current_num += 1
        sum_divisors = 0


def print_perfect_numbers():
    # prints perfects numbers

    generator_iterator = check_divisors()
    for number in range(10):
        print(next(generator_iterator))


if __name__ == '__main__':
    print_perfect_numbers()
