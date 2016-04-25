# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt

def histopi(datas):
  dataset = []
  for i in range(10):
    dataset.append(0)
  for data in datas:
    dataset[data] += 1
  plt.hist(datas, bins=(-0.5,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5))
  plt.xlabel('pi digits')
  plt.ylabel('ocurence')
  plt.axis([-1, 10, 0, 115000])
  plt.savefig("histopi.png", bbox_inches='tight')
  return dataset


