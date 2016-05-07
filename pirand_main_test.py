# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from tools import piLoader, latex
import pirand
import random
from continuous_tests import poker, khi2, gap

pirand_data = [pirand.next() for x in range(int(1e6))]
python_data = [random.random() for x in range(int(1e6))]


def comparative_histogram():
    piFile = piLoader.piDigits()
    piRand = map(lambda x: x*10, pirand_data)

    """Creates a discrete dataset from datas and draw the linked histogram"""
    plt.hist(piFile, bins=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), color="lightblue", linewidth=0, width=1)
    plt.hist(piRand, bins=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), color="red",linewidth=0, width=0.5)
    plt.xlabel('pi digits')
    plt.ylabel('ocurence')
    plt.axis([0, 10, 0, 115000])
    plt.savefig("assets/test.png", bbox_inches='tight')

def khi2_test():
    print '%' + '-' * 69 + '\n' + '% KHI2 TEST\n' + '%' + '-' * 69 + '\n'
    dataset1 = khi2.dataset(pirand_data)
    dataset2 = khi2.dataset(python_data)
    print latex.table_generator('classes', [dataset1, dataset2], [[1e5]*10], 1, ["$\pi$ rand", "Python rand"])
    print latex.khi2_table_generator([khi2.k(dataset1), khi2.k(dataset2)], 10, ["\pi", "Python"])


def gap_test():
    print '%' + '-' * 69 + '\n' + '% GAP TEST\n' + '%' + '-' * 69 + '\n'
    datasets = [gap.test_ab(pirand_data, 0., 0.5, 15), gap.test_ab(python_data, 0., 0.5, 15)]
    theoretical_values = [gap.theoretical_effective_ab(datasets[0], 15, 0., 0.5), gap.theoretical_effective_ab(datasets[1], 15, 0., 0.5)]
    print latex.table_generator("longueur du gap", datasets, theoretical_values, 0, ["$\pi$ rand", "Python rand"])
    khi_gaps = [khi2.k(datasets[0], theoretical_values[0]), khi2.k(datasets[1], theoretical_values[0])]
    print latex.khi2_table_generator(khi_gaps, len(datasets[0]), ["\pi", "Python"])

def poker_test():
    print '%' + '-' * 69 + '\n' + '% POKER TEST\n' + '%' + '-' * 69 + '\n'
    dataset1 = poker.observed_classes(poker.dataset(pirand_data))
    dataset2 = poker.observed_classes(poker.dataset(python_data))
    theoretical_datatset = poker.theoretical_classes()
    print latex.table_generator('classes', [dataset1,dataset2],[theoretical_datatset, theoretical_datatset], 0, ["$\pi$ rand", "Python rand"])


#khi2_test()
#gap_test()
poker_test()