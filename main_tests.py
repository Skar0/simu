from continuous_tests import khi2, gap, coupons, poker
from tools import piLoader, latex

data = piLoader.piDigits()


def khi2_test():
    print '%' + '-' * 69 + '\n' + '% KHI2 TEST\n' + '%' + '-' * 69 + '\n'
    dataset = khi2.histopi(data)
    print latex.table_generator("r", [dataset], [10 * [100000]])
    k = khi2.k(dataset)
    print latex.khi2_table_generator([k], len(dataset)), '\n'


def gap_test(digit):
    print '%' + '-' * 69 + '\n' + '% GAP TEST\n' + '%' + '-' * 69 + '\n'
    gap.histopi(data, digit)
    dataset = gap.test(data, digit)
    theoretical_values = gap.theoretical_effective(dataset, 80)
    print latex.table_generator("longueur du gap", [dataset], [theoretical_values], 0)
    khi_gap = khi2.k(dataset, theoretical_values)
    print latex.khi2_table_generator([khi_gap], len(dataset)), '\n'


def coupons_test():
    print '%' + '-' * 69 + '\n' + '% COUPONS TEST\n' + '%' + '-' * 69 + '\n'
    coupons_data = coupons.make_classes(100, data)

    samples_number = coupons_data[0]
    observed_classes = coupons_data[1]

    theoretical_classes = coupons.theoretical(100, 10, samples_number)

    khi = khi2.k(observed_classes[10:], theoretical_classes[10:])
    print latex.table_generator("longueur de la sequence", [observed_classes[10:]], [theoretical_classes[10:]])
    print latex.khi2_table_generator([khi], len(observed_classes)), '\n'
    coupons.comparative_histogram(observed_classes, theoretical_classes)


def poker_test():
    print '%' + '-' * 69 + '\n' + '% POKER TEST\n' + '%' + '-' * 69 + '\n'
    theoretical_classes = poker.theoretical_classes()
    observed_classes = poker.observed_classes(data)

    khi = khi2.k(observed_classes,theoretical_classes)
    print latex.table_generator("Nombre de digits differents", [observed_classes], [theoretical_classes])
    print latex.khi2_table_generator([khi], len(observed_classes)), '\n'

khi2_test()
gap_test(5)
coupons_test()
poker_test()
