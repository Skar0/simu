# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy
from tools import piLoader, latex
import pirand
import random
from tests import poker, khi2, gap, coupons, kolmogorov
import matplotlib.pyplot as plt
import numpy as numpy

pirand_data = [pirand.next() for x in range(int(1e6))]
python_data = [random.random() for x in range(int(1e6))]


def comparative_histogram():
    """Create an histogram of pirand_data and python_data"""
    dataset = khi2.dataset(pirand_data)
    dataset2 =  khi2.dataset(python_data)
    fig, ax = plt.subplots()
    pirand_observed = ax.bar(map(lambda x: x * 0.1 - 0.04, range(10)), dataset, color="firebrick", width=0.04)
    python_observed = ax.bar(map(lambda x: x * 0.1, range(10)), dataset2, color="orangered", width=0.04)
    plt.legend([pirand_observed, python_observed], ["generateur pirand", "generateur python"])
    plt.xlabel('classe')
    plt.ylabel('occurrence')
    ax.set_xticklabels(('???', '[0.0, 0.1[', '[0.2, 0.3[', '[0.4, 0.5[', '[0.6, 0.7[', '[0.8, 0.9['))
    plt.axis([-0.07, 0.97, 0, 130000])
    plt.savefig("report/comparative_histogram.png", bbox_inches='tight')


def khi2_test():
    print '%' + '-' * 69 + '\n' + '% KHI2 TEST\n' + '%' + '-' * 69 + '\n'
    dataset1 = khi2.dataset(pirand_data)
    dataset2 = khi2.dataset(python_data)
    print latex.table_generator('classes', [dataset1, dataset2], [[1e5]*10], 1, ["$\pi$ rand", "Python rand"])
    print latex.khi2_table_generator([khi2.k(dataset1), khi2.k(dataset2)], 10, ["\pi", "Python"])
    print '\n'


def gap_test():
    print '%' + '-' * 69 + '\n' + '% GAP TEST\n' + '%' + '-' * 69 + '\n'
    datasets = [gap.test_ab(pirand_data, 0., 0.5, 15), gap.test_ab(python_data, 0., 0.5, 15)]
    theoretical_values = [gap.theoretical_effective_ab(datasets[0], 15, 0., 0.5), gap.theoretical_effective_ab(datasets[1], 15, 0., 0.5)]
    print latex.table_generator("longueur du gap", datasets, theoretical_values, 0, ["$\pi$ rand", "Python rand"])
    khi_gaps = [khi2.k(datasets[0], theoretical_values[0]), khi2.k(datasets[1], theoretical_values[0])]
    print latex.khi2_table_generator(khi_gaps, len(datasets[0]), ["\pi", "Python"])
    print '\n'


def poker_test():
    print '%' + '-' * 69 + '\n' + '% POKER TEST\n' + '%' + '-' * 69 + '\n'
    dataset1 = poker.observed_classes(poker.dataset(pirand_data))
    dataset2 = poker.observed_classes(poker.dataset(python_data))
    theoretical_dataset = poker.theoretical_classes()
    print latex.table_generator('classes', [dataset1,dataset2],[theoretical_dataset, theoretical_dataset], 0, ["\piRand", "Python rand"])
    khi_pirand = khi2.k(dataset1,theoretical_dataset)
    khi_python = khi2.k(dataset2,theoretical_dataset)
    print latex.khi2_table_generator([khi_pirand,khi_python],len(dataset1),["\piRand", "Python"])
    print '\n'

    plt.clf()
    theo = plt.bar(numpy.arange(len(theoretical_dataset)), theoretical_dataset, color="darkgreen", width=0.33,linewidth=0)
    obs1 = plt.bar(numpy.arange(len(dataset1)) + 0.33, dataset1, color="lightblue", width=0.33,linewidth=0)
    obs2 = plt.bar(numpy.arange(len(dataset2)) + 0.66, dataset2, color="red", width=0.33, linewidth=0)
    plt.xlabel(u'Nombre de chiffres différents dans la séquence')
    plt.ylabel("Nombre d'occurences")
    plt.legend((theo, obs1,obs2), (u'Valeurs théoriques', u'Valeurs observées $\pi Rand$ ',u'Valeurs observées python '),loc=2)
    plt.axis([0, len(theoretical_dataset), 0, max(theoretical_dataset) + 5000])
    plt.savefig("report/poker_generator_histogram.png", bbox_inches='tight')


def kolmogorov_test():
    print '%' + '-' * 69 + '\n' + '% KOLMOGOROV TEST\n' + '%' + '-' * 69 + '\n'
    kolmo_100 = [kolmogorov.kolmo(pirand_data[:100], kolmogorov.theoretical_distribution),
                 kolmogorov.kolmo(python_data[:100], kolmogorov.theoretical_distribution)]
    kolmo_1000 = [kolmogorov.kolmo(pirand_data[:1000], kolmogorov.theoretical_distribution),
                  kolmogorov.kolmo(python_data[:1000], kolmogorov.theoretical_distribution)]
    kolmo_10000 = [kolmogorov.kolmo(pirand_data[:10000], kolmogorov.theoretical_distribution),
                   kolmogorov.kolmo(python_data[:10000], kolmogorov.theoretical_distribution)]
    """
    kolmo_100000 = [kolmogorov.kolmo(pirand_data[:100000], kolmogorov.theoretical_distribution),
                    kolmogorov.kolmo(python_data[:100000], kolmogorov.theoretical_distribution)]
    """
    kolmo_values = [kolmo_100,kolmo_1000,kolmo_10000]

    kolmo_sizes = [100,1000,10000]

    print latex.kolmogorov_table_generator(kolmo_values,kolmo_sizes)
    print '\n'


comparative_histogram()
khi2_test()
gap_test()
poker_test()
kolmogorov_test()