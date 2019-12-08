#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program rounds decimal numbers to a decimal point

import random


def main():
    # This function generates random numbers and find their average

    random_list = []
    random_number = 0
    average = 0

    while random_number <= 10:
        my_random_number = random.randint(1, 9+1)
        random_list.append(my_random_number)
        print(random_list, end="")
        average = (average + my_random_number)/2
        print("")
        random_number += 1

    print("the average of the numbers is: ", average)


if __name__ == '__main__':
    main()
