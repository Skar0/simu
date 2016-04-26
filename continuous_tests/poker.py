# -*- coding: utf-8 -*-


def occurrence_counter2(number):
    """Counts the number of different digits in a number"""
    occurrences = []
    for digit in str(number):
        if digit not in occurrences:
            occurrences.append(digit)
    return len(occurrences)


def occurrence_counter(number):
    """Counts the number of different digits in a number"""
    occurrences = []
    for digit in number:
        if digit not in occurrences:
            occurrences.append(digit)
    return len(occurrences)


def poker_test(numbers):
    """Transforms a list of numbers into a list of 5-digits integers"""
    n = len(numbers)
    classes = [0, 0, 0, 0, 0]

    i = 0
    stop = n-5
    while i <= stop:
        number = numbers[i:(i+5)]
        classes[occurrence_counter(number)-1] += 1
        i+=5

    return classes





def stirling(k,r):
    if k==r or r==1:
        return 1
    return stirling(k-1,r-1) + r*stirling(k-1,r)

test = [1,2,3,4,5,  7,7,7,7,7, 8,9,9,8,0]
print poker_test(test)
