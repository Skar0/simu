from continuous_tests import khi2, gap
import latex
from tools import piLoader

datas = piLoader.piDigits()
dataset = khi2.histopi(datas)
print latex.table_generator("r", dataset, 10 * [10000])
k = khi2.k(dataset)
print latex.khi2_table_generator(k, len(dataset))
gap.histopi(datas, 0, 5)
