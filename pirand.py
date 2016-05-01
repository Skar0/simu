# -*- coding: utf-8 -*-
import time
import math
from tools import piLoader

index = []
pi_digits = piLoader.piDigits()

def reverse(n):
    """reverse the digits of the integer n
       example : reverse(1234) = 4321"""
    def reverse_rec(n, acc):
        if n == 0:
            return acc
        else:
            return reverse_rec(n // 10, acc * 10 + n % 10)
    return reverse_rec(n, 0)

def next():
    """generates a pseudo random float ϵ [0, 1[ following the 1M digits of pi"""
    global index
    if index == []:
        for i in range(16):
            index.append(reverse(int(time.time() * 1e6 % 1e6)))
    else:
        index = map(lambda x: int((x + 1) % 1e6), index)
    def generate_number(i, acc):
        if i >= 16:
            return acc/1e16
        else:
            return generate_number(i+1, acc + pi_digits[index[i]] * 10 ** (16-(i+1)))
    return generate_number(0, 0.)
