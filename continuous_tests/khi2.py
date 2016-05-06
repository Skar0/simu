# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt

def histopi(data):
    """Creates a discrete dataset from datas and draw the linked histogram"""
    dataset = discrete_dataset(data)
    plt.hist(data, bins=(-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5))
    plt.xlabel('pi digits')
    plt.ylabel('occurrence')
    plt.axis([-1, 10, 0, 115000])
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
