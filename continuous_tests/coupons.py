# -*- coding: utf-8 -*-


def count(dataset):
    temp = []
    data = []
    length =[]
    nbr =0
    for digit in dataset:
        data.append(digit)
        if digit not in temp:
            temp.append(digit)
        if len(temp) == 10:
            temp = []
            i = len(data)
            try :
                length[i]
            except IndexError:
                for j in range(i+1-len(length)):
                    length.append(0)
            finally:
                length[i] +=1
                nbr +=1


