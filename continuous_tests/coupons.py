# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt
import latex
from continuous_tests import poker
from tools import piLoader
from continuous_tests import khi2


def count(dataset):
    temp = []
    data = []
    length =[]
    nbr =0
    for digit in dataset:
        data.append(digit)
        if digit not in temp:
            temp.append(digit)
        if len(temp) == 10:
            temp = []
            i = len(data)
            data = []
            try :
                length[i]
            except IndexError:
                for j in range(i+1-len(length)):
                    length.append(0)
            finally:
                length[i] +=1
                nbr +=1
    return (nbr, length)
"""seq r de long, d digits, sur x echantillons"""
def theoretical(r, d, n):
    probas = []
    for i in range(n):
        probas.append(0)
        """prob est 0 avant 10"""
    for j in range(10,r):
        prob = (float(math.factorial(d))/math.pow(d,j))*poker.stirling(j-1,d-1)
        probas[j] = prob
    return map(lambda x: x*n, probas)


def histo(expected, actual):
    plt.clf()
    plt.bar(1, expected, color="blue", linewidth =0, width = 0.6, alpha = 0.5)
    plt.bar(1.1, actual, color="red", linewidth=0, width=0.6, alpha=0.5)
    plt.xlabel('Longueur de la sequence')
    plt.ylabel('occurrence')
    plt.axis([0, len(expected), 0, max(expected) + 1000])
    plt.savefig("assets/coupon_histo.png", bbox_inches='tight')


