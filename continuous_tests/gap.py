# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math

def test(datas, digit):
  """Computes the effective gap test for the digit in parameter
     datas : the list of discrete values ϵ [0, 9]
     digit : the digit on which apply the test"""
  l = []
  current_length = 0
  for data in datas:
    if data != digit:
      current_length += 1
    else:
      l.append(current_length)
      current_length = 0
  max_length = max(l)
  dataset = [0] * (max_length + 1)
  for i in range(max_length + 1):
    dataset[i] = l.count(i)
  return dataset

def gap_dataset(datas, a, b):
  """deprecated : for non-discrete values"""
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

def histopi(datas, digit):
  """Creates a histogram showing the gap lengths for the digit in parameter
     datas : the list of discrete datas (integer) ϵ [0, 9]
     digit : the digit on which the gap test is based"""
  dataset = test(datas, digit)
  print dataset
  plt.clf()
  plt.bar(range(len(dataset)), dataset, color="red")
  plt.xlabel('longueur du gap')
  plt.ylabel('occurrence')
  plt.axis([0, len(dataset), 0, max(dataset)+1000])
  plt.savefig("assets/gap_histopi.png", bbox_inches='tight')

def theoretical_effective(dataset, gap_limit):
  """Computes the theoritical value of the gap test.
     dataset : the gap count list
     gap_limit : the length of the gap limit"""
  n = sum(dataset)
  l = [0] * len(dataset)
  for i in range(len(dataset)):
    l[i] = math.pow(0.9, min(i, gap_limit)) * 0.1 * n
  return l
