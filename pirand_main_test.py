# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from tools import piLoader, latex
import pirand
import random
from continuous_tests import poker, khi2


def getPiRand(n):
    temp = []
    for i in range (0, n):
        temp.append(pirand.next())
    return temp


def comparative_histogram():
    piFile = piLoader.piDigits()
    rand = getPiRand(int(1e6))
    piRand = map(lambda x: x*10, rand)

    """Creates a discrete dataset from datas and draw the linked histogram"""
    plt.hist(piFile, bins=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), color="lightblue", linewidth=0, width=1)
    plt.hist(piRand, bins=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), color="red",linewidth=0, width=0.5)
    plt.xlabel('pi digits')
    plt.ylabel('ocurence')
    plt.axis([0, 10, 0, 115000])
    plt.savefig("assets/test.png", bbox_inches='tight')

def khi2_test():
    dataset1 = khi2.dataset([pirand.next() for x in range(int(1e6))])
    dataset2 = khi2.dataset([random.random() for x in range(int(1e6))])
    print latex.table2_generator('classes', dataset1, dataset2, [1e5]*10, "$\pi$ rand", "Python rand")
    print latex.khi2_table_generator([khi2.k(dataset1), khi2.k(dataset2)], 10, ["\pi", "Python"])


khi2_test()