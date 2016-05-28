# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt
import numpy

def histopi(data):
    """Creates a discrete dataset from data and draw the linked histogram"""
    dataset = discrete_dataset(data)
    theoretical_dataset = [theoretical_effective(dataset)]*10
    observed = plt.bar(numpy.arange(len(dataset)) - 0.4, dataset, color="blue", width=0.4)
    theoretical = plt.bar(numpy.arange(len(theoretical_dataset)), theoretical_dataset, color="deepskyblue", width=0.4)
    plt.legend([observed, theoretical], ["effectifs observes", "effectifs theoriques"])
    plt.xlabel('pi digits')
    plt.ylabel('occurrence')
    plt.axis([-0.7, 9.7, 0, 130000])
    plt.savefig("report/khi2_histopi.png", bbox_inches='tight')
    return dataset


def discrete_dataset(data):
    """Creates a discrete dataset from data"""
    dataset = [0] * 10
    for value in data:
        dataset[value] += 1
    return dataset


def dataset(data):
    """Creates a non-discrete dataset from data ϵ [0, 1[ of length 10"""
    dataset = [0] * 10
    for value in data:
        dataset[int(value * 10)] += 1
    return dataset


def sumf(f, i, j):
    """definition of the sum : ∑(i ≤ j) f(i)"""
    def sumrec(i, acc):
        if i > j:
            return acc
        else:
            return sumrec(i + 1, acc + f(i))
    return sumrec(i, 0)

def theoretical_effective(dataset):
    """computes the uniform law value on the dataset"""
    return float(sum(dataset))/len(dataset)

def k(dataset, effective=[]):
    if effective == [] :
        effective = [theoretical_effective(dataset)] * len(dataset)
    f = lambda i: ((dataset[i] - effective[i])/math.sqrt(effective[i]))**2
    return sumf(f, 0, len(dataset) - 1)
