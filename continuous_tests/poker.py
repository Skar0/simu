# -*- coding: utf-8 -*-
import math
import random

import latex
from continuous_tests import khi2
from tools import piLoader

known_stirling_values = []
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


def observed_classes(numbers):
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

def theoritical_classes():
    i = 5
    d =10
    theo_proba = [0]*5
    for j in range(1,i+1):
        stir = stirling(i,j)
        for t in range(0,j):
            stir *= (d-t)
        theo_proba[j-1]= stir/math.pow(d,i)

    return map(lambda x: x*(1000000/i),theo_proba)


def stirling(k,r):
    try:
        known_stirling_values[k]
    except IndexError:
        for i in range(k+1-len(known_stirling_values)):
            known_stirling_values.append([])
    try:
        known_stirling_values[k][r]
    except IndexError:
        for i in range(r+1-len(known_stirling_values[k])):
            known_stirling_values[k].append(None)

    if k==r or r==1:
        return 1
    if(known_stirling_values[k][r] == None):
        known_stirling_values[k][r] = stirling(k-1,r-1) + r*stirling(k-1,r)
    return known_stirling_values[k][r]

def test():
    pi = piLoader.piDigits()
    theor = theoritical_classes()
    obs = observed_classes(pi)

    return khi2.k(obs,theor)


"""
print test()


pi = piLoader.piDigits()
print latex.table_generator("r",observed_classes(pi),theoritical_classes())


pi2=""
for j in range(1000000):
    k = random.randint(0,9)
    pi2+=str(k)


print observed_classes(pi2)
"""