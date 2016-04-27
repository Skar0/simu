# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math

def gap(datas, a, b):
  l = []
  current_length = 0
  for data in datas:
    if data < a or data > b:
      current_length += 1
    else:
      l.append(current_length)
      current_length = 0
  max_length = max(l)
  dataset = [0] * (max_length + 1)
  for i in range(max_length + 1):
    dataset[i] = l.count(i)
  return dataset

def histopi(datas, a, b):
  dataset = gap(datas, a, b)
  print dataset
  plt.clf()
  plt.bar(range(len(dataset)), dataset, color="red")
  plt.xlabel('longueur du gap')
  plt.ylabel('ocurence')
  plt.axis([0, len(dataset), 0, max(dataset)+10000])
  plt.savefig("gap_histopi.png", bbox_inches='tight')

def theorical_effective(dataset, a, b):
  n = sum(dataset)
  p = float(b - a) / 9
  l = [0] * len(dataset)
  for i in range(len(l)):
    l[i] = math.pow((1 - p), i) * n * p
  return l
