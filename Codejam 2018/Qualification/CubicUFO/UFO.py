# -*- coding: utf-8 -*-
"""
Created on Fri May  4 23:22:30 2018

@author: Wilson
"""

import math

def ufo(A):
    if A <= 2**0.5:
        alpha = math.pi/4 - math.acos(A/(2**0.5))
        x = math.sin(alpha)/2
        y = math.cos(alpha)/2
        return ['0 0 0.5', ' '.join([str(-x), str(y), '0']), ' '.join([str(y), str(x), '0'])]
    return ['0','0','0']

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    A = float(input())
    result = ufo(A)
    print("Case #{}:".format(i))
    for r in result:
        print("{}".format(r))