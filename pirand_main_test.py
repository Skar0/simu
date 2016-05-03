# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from tools import piLoader
import pirand as piRand
from continuous_tests import poker

def getPiRand(n):
    temp = []
    for i in range (0, n):
        temp.append(piRand.next())
    return temp


def comparative_histogram():
    piFile = piLoader.piDigits()
    rand = getPiRand(1000000)
    piRand = map(lambda x: x*10, rand)

    """Creates a discrete dataset from datas and draw the linked histogram"""
    plt.hist(piFile, bins=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), color="lightblue", linewidth=0, width=1)
    plt.hist(piRand, bins=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), color="red",linewidth=0, width=0.5)
    plt.xlabel('pi digits')
    plt.ylabel('ocurence')
    plt.axis([0, 10, 0, 115000])
    plt.savefig("assets/test.png", bbox_inches='tight')

comparative_histogram()