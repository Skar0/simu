# -*- coding: utf-8 -*-


def occurrence_counter(number):
    """Counts the number of different digits in a number"""
    occurrences = []
    for digit in str(number):
        if digit not in occurrences:
            occurrences.append(digit)
    return len(occurrences)

print occurrence_counter(6239111)