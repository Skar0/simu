# -*- coding: utf-8 -*-
from tools import piLoader as loader


def kolmogorov(data, theoretical_distribution):
    n = len(data)
    empirical = []
    cumulative = []
    gaps = []

    i = 0
    nbr_of_digits = 10
    while i < nbr_of_digits:
        empirical.append(empirical_distribution(data, i, n))
        cumulative.append(theoretical_distribution(i))
        gaps.append(abs(empirical[i]-cumulative[i]))
        print(gaps[i])
        i+=1
    max_gap = max(gaps)
    return max_gap


def empirical_distribution(data, x, n):
    i = 0
    acc = 0
    while i < n:
        if data[i] <= x:
            acc+=1
        i+=1
    return float(acc)/n


def theoretical_distribution(x):
    a = 0
    b = 1
    if x < a:
        return 0
    elif x > b:
        return 1
    else:
        return float(x - a) / (b - a)

print kolmogorov(loader.piDigits(), theoretical_distribution)
