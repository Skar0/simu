from continuous_tests import khi2, gap
import latex
from tools import piLoader

datas = piLoader.piDigits()

def khi2_test():
  dataset = khi2.histopi(datas)
  print latex.table_generator("r", dataset, 10 * [10000])
  k = khi2.k(dataset)
  print latex.khi2_table_generator(k, len(dataset))

def gap_test(digit):
  gap.histopi(datas, digit)
  dataset = gap.test(datas, digit)
  theoretical_values = gap.theoretical_effective(dataset, 80)
  print latex.table_generator("longueur du gap", dataset, theoretical_values, 0)
  khi_gap = khi2.k(dataset, theoretical_values)
  print latex.khi2_table_generator(khi_gap, len(dataset))

khi2_test()
gap_test(5)
