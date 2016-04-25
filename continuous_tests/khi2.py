import math
import matplotlib.pyplot as plt

def histopi(datas):
  dataset = []
  for i in range(10):
    dataset.append([0])
  for data in datas:
    dataset[data] += 1
  histo = plt.hist(data, bin = 10)
  plt.clf()
  plt.xlabel('pi digits')
  plt.ylabel('ocurence')
  plt.axis([0, 10, 0, 20000])
  plt.savefig("histopi.png", bbox_inches='tight')
  return dataset


