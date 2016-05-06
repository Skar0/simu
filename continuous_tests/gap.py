# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math


def test(datas, digit, gap_limit=80):
    """Computes the effective gap test for the digit in parameter
       datas : the list of discrete values ϵ [0, 9]
       digit : the digit on which apply the test
       gap_limit : the limit of the gap (must be inferior than the max gap)"""
    l = []
    current_length = 0
    for data in datas:
        if data != digit:
            current_length += 1
        else:
            l.append(current_length)
            current_length = 0
    max_length = max(l)
    dataset = [0] * (max_length + 1)
    for i in range(max_length + 1):
        dataset[i] = l.count(i)
    dataset = dataset[:gap_limit + 1] + [sum(dataset[gap_limit + 1 :])]
    return dataset


def test_ab(datas, a, b, gap_limit=80):
    """Computes the effective gap test for the interval [a, b] in parameter
       datas : the list of values ϵ [0, 1[
       [a, b] : the interval on which apply the test
       gap_limit = the gap limit (must be inferior than the max gap)"""
    l = []
    current_length = 0
    for data in datas:
        if data < a or data > b:
            current_length += 1
        else:
            l.append(current_length)
            current_length = 0
    max_length = max(l)
    dataset = [0] * (max_length + 1)
    for i in range(max_length + 1):
        dataset[i] = l.count(i)
    dataset = dataset[:gap_limit + 1] + [sum(dataset[gap_limit + 1 :])]
    return dataset


def histopi(datas, digit):
    """Creates a discrete-values histogram showing the gap lengths for the digit in parameter
       datas : the list of discrete datas (integer) ϵ [0, 9]
       digit : the digit on which the gap test is based"""
    dataset = test(datas, digit)
    theoretical_dataset = theoretical_effective(dataset, 80)
    plt.clf()
    plt.bar(range(len(dataset)), dataset, color="red", linewidth=0, width=1, alpha=0.5)
    plt.bar(range(len(theoretical_dataset)), theoretical_dataset, color="blue", linewidth=0, width=0.5, alpha=0.5)
    plt.xlabel('longueur du gap')
    plt.ylabel('occurrence')
    plt.axis([0, len(dataset), 0, max(dataset)+1000])
    plt.savefig("report/gap_histopi.png", bbox_inches='tight')


def theoretical_effective(dataset, gap_limit):
    """Computes the theoritical value of the discrete gap test.
       dataset : the gap count list
       gap_limit : the length of the gap limit"""
    n = sum(dataset)
    l = [0] * len(dataset)
    for i in range(len(dataset)):
        if i <= gap_limit:
            l[i] = math.pow(0.9, i) * 0.1 * n
        else:
            l[i] = math.pow(0.9, gap_limit + 1) * n
    return l


def theoretical_effective_ab(dataset, gap_limit, a, b):
    """Computes the theoritical value of the gap test for an interval [a, b]
       dataset : the gap count list
       gap_limit : the length of the gap limit
       [a, b] : the interval on which apply the gap test"""
    n = sum(dataset)
    l = [0] * len(dataset)
    p = b - a
    for i in range(len(dataset)):
        if i <= gap_limit:
            l[i] = math.pow(1 - p, i) * n * p
        else:
            l[i] = math.pow(1 - p, gap_limit + 1) * n
    return l
