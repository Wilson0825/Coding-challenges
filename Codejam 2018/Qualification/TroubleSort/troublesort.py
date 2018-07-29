# -*- coding: utf-8 -*-
"""
Created on Fri May  4 23:21:59 2018

@author: Wilson
"""

def TroubleSort(L):
    done = False
    while not done:
        done = True
        for i in range(len(L)-2):
            if L[i] > L[i+2]:
                done = False
                L[i:i+3] = L[i:i+3][::-1]
    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            return str(i)
    return 'OK'

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    k = int(input())
    l = list([int(s) for s in input().split(" ")])
    print("Case #{}: {}".format(i, TroubleSort(l)))
