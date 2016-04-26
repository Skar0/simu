import continuous_tests.khi2 as khi2
import latex
from tools import piLoader

dataset = khi2.histopi(piLoader.piDigits())
print dataset
print latex.table_generator("r", dataset, 10 * [10000])
k = khi2.k(dataset)
print latex.khi2_table_generator(k, len(dataset))
