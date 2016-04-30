# -*- coding: utf-8 -*-

def piDigits():
    """Loads all pi digits and returns them in a list"""
    file = open("assets/pi6.txt")
    next(file)
    digits = []
    for line in file :
        for digit in line:
            if digit != '\n' : digits.append(int(digit))

    file.close()
    return digits
