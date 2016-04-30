from continuous_tests import khi2, gap, coupons, poker
from tools import piLoader, latex

data = piLoader.piDigits()

def khi2_test():
    dataset = khi2.histopi(data)
    print latex.table_generator("r", dataset, 10 * [10000])
    k = khi2.k(dataset)
    print latex.khi2_table_generator(k, len(dataset))

def gap_test(digit):
    gap.histopi(data, digit)
    dataset = gap.test(data, digit)
    theoretical_values = gap.theoretical_effective(dataset, 80)
    print latex.table_generator("longueur du gap", dataset, theoretical_values, 0)
    khi_gap = khi2.k(dataset, theoretical_values)
    print latex.khi2_table_generator(khi_gap, len(dataset))


def coupons_test():
    coupons_data = coupons.count(data)

    effective = c[1]
    samples = c[0]

    theo = theoretical(len(effective), 10, samples)

    khi = khi2.k(effective[10:], theo[10:])
    print "khi 2 test result = " + str(khi)
    print latex.table_generator("r", effective[10:], theo[10:])
    print latex.khi2_table_generator(khi, len(effective))
    histo(effective, theo)

khi2_test()
gap_test(5)
coupons_test()
