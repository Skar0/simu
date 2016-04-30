# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt
from continuous_tests import poker


def make_classes(dataset):
    """Goes sequentially trough the set of data, making sequences of numbers. Each sequence of number is increased in
     size using the next available digit in the set of data until all possible digits appear at least once in the
     sequence. The size of this sequence is then added an array. We thus obtain an array where at the position n is
     n is stored the number of n-long sequences. We return the number of sequences and the array of classes."""
    temp = [] # The array storing the unique digits already in the sequence
    data = [] # The array in which the sequence is built
    length = [] # The array containing the classes
    nbr = 0 # The number of built sequences

    for digit in dataset:
        # For each digit in the dataset we add it to the current sequence
        data.append(digit)

        # If the digit was not already in the sequence, we add it to temp
        if digit not in temp:
            temp.append(digit)

        # If temp length is 10, all ten digits are in the sequence, we need to add the length of the sequence
        if len(temp) == 10:
            # We have all digits, we reset the temp and data arrays
            temp = []
            i = len(data)
            data = []

            # We try to add the length of the sequence, if the length array was too small, we make it bigger
            try:
                length[i]
            except IndexError:
                for j in range(i + 1 - len(length)):
                    length.append(0)
            # If sequence length is i, we increment length[i] and we increment nbr to signal we have one more sample
            finally:
                length[i] += 1
                nbr += 1
    return nbr, length


def theoretical(r, d, n):
    """Computes the theoretical classes obtained for the coupons test from the length r of the sequence of digits,
    the number d of possible digits and the number n of samples"""
    probas = []
    # Initially the list is empty
    for i in range(n):
        probas.append(0)
    # Probability to have all 10 digits is 0 before the sequence is 10 digits long
    for j in range(10, r):
        # All other probabilities are computed with the formula provided in the course
        prob = (float(math.factorial(d)) / math.pow(d, j)) * poker.stirling(j - 1, d - 1)
        probas[j] = prob
    # Multiplying the probability with the number n of samples to obtain the theoretical classes
    return map(lambda x: x * n, probas)


def comparative_histogram(theoretical, observed):
    """Builds a comparative histogram between the theoretical and observed classes obtained by the test"""
    plt.clf()
    plt.bar(range(len(theoretical)), theoretical, color="blue", linewidth=0, width=0.6, alpha=0.5)
    plt.bar(range(len(observed)), observed, color="red", linewidth=0, width=0.6, alpha=0.5)
    plt.xlabel('Longueur de la sequence')
    plt.ylabel("Nombre d'occurences")
    plt.axis([0, len(theoretical), 0, max(theoretical) + 1000])
    plt.savefig("assets/coupons_histogram.png", bbox_inches='tight')
