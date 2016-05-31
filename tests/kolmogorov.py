# -*- coding: utf-8 -*-
from tools import piLoader as loader


def kolmo(data, theoretical_distribution):
    n = len(data)
    sorted_data = sorted(data)
    empirical = []
    cumulative = []
    gaps = []

    j = 0
    for number in sorted_data:
        empirical.append(empirical_distribution(sorted_data, number, n))
        cumulative.append(theoretical_distribution(number))
        gaps.append(abs(empirical[j]-cumulative[j]))
        j+=1
    max_gap = max(gaps)
    return max_gap


def empirical_distribution(data, x, n):
    i = 0
    while i < n and data[i] <= x:
      i+=1
    return float(i)/n


def theoretical_distribution(x):
    a = 0
    b = 1
    if x < a:
        return 0
    elif x > b:
        return 1
    else:
        return float(x - a) / (b - a)
