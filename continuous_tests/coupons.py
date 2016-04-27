# -*- coding: utf-8 -*-
import math

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
    for j in range(10,n):
        prob = (math.factorial(d)/math.pow(d,r))*poker.stirling(r-1,d-1)
        probas[j] = prob
    return map(lambda x: x*n, probas)

def test():
    pi = piLoader.piDigits()
    effective = count(pi)
    effectiveval = effective[1]
    theo = theoretical(10,10,effective[0])

    return khi2.k(effectiveval,theo)

print test()
