# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt
import numpy as numpy
# Used to optimise stirling values

known_stirling_values = []


def occurrence_counter(number):
    """Counts the number of different digits in a number"""
    occurrences = []
    for digit in number:
        if digit not in occurrences:
            occurrences.append(digit)
    return len(occurrences)


def observed_classes(numbers):
    """Transforms a list of numbers into 5-digits sequences, counts the number of different digits in those sequences
    and increments the corresponding position in an array. We thus obtain classes (1 : all same digits, 2 : two
    different digits in the sequence, ... , 5 : all different digits)"""

    # Number of digits
    n = len(numbers)
    classes = [0, 0, 0, 0, 0]

    i = 0
    stop = n-5 # Last possible sequence starts at n-5
    while i <= stop:
        number = numbers[i:(i+5)] # We take a 5 digits long sequence
        classes[occurrence_counter(number)-1] += 1
        i += 5

    return classes


def theoretical_classes():
    """Computes the theoretical classes for the poker test"""
    i = 5 # Sequence length
    d = 10 # Number of possible different digits
    theoretical_probas = [0]*i # We have a probability to have all the same digits in the sequence, two different, ect

    # Probabilities are computed from the formula given in the course
    for j in range(1,i+1):
        stir = stirling(i,j)
        for t in range(0,j):
            stir *= (d-t)
        theoretical_probas[j-1]= stir/math.pow(d,i)

    # Multiplying probabilities with the number of samples to obtain the theoretical classes
    return map(lambda x: x*(1000000/i),theoretical_probas)


def stirling(k,r):
    """Computes the stirling number for k and r"""
    # This version is optimised using a known-values array (we try if the value is known before computing it)
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

    if known_stirling_values[k][r] is None:
        known_stirling_values[k][r] = stirling(k-1,r-1) + r*stirling(k-1,r)
    return known_stirling_values[k][r]


def dataset(data):
    """Transforms non discrete values ϵ [0,1[ data list into discrete values list ϵ [0,9] """
    return map(lambda x : int(x * 10), data)

def comparative_histogram(theoretical, observed):
    """Builds a comparative histogram between the theoretical and observed classes obtained by the test"""
    plt.clf()
    theo = plt.bar(numpy.arange(len(theoretical)), theoretical, color="darkgreen", width=0.5,linewidth=0)
    obs = plt.bar(numpy.arange(len(observed)) + 0.5, observed, color="yellowgreen", width=0.5,linewidth=0)
    plt.xlabel(u'Nombre de chiffres différents dans la séquence')
    plt.ylabel("Nombre d'occurences")
    plt.legend((theo, obs), (u'Valeurs théoriques', u'Valeurs observées'),loc=2)
    plt.axis([0, len(theoretical), 0, max(theoretical) + 5000])
    plt.savefig("report/poker_histogram.png", bbox_inches='tight')