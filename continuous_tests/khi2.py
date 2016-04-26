# -*- coding: utf-8 -*-
import math

def sumf(f, i, j):
  """definition of the sum : ∑(i ≤ j) f(i)"""
  def sumrec(i, acc):
    if i > j:
      return acc
    else:
      return sumrec(i + 1, acc + f(i))
  return sumrec(i, 0)

def k(dataset):
  effective = float(sum(dataset))/len(dataset)
  f = lambda i: ((dataset[i] - effective)/math.sqrt(effective))**2
  return sumf(f, 0, len(dataset) - 1)
