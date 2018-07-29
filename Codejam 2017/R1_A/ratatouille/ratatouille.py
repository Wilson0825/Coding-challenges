# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 00:09:23 2017

@author: Wilson
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:52:21 2017

@author: Wilson
"""
from operator import itemgetter
import math

data = []
with open("C:/Users/Wilson/Desktop/Codejam 2017/R1_A/ratatouille/B-large.in", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(int, line.split(' '))))

data.pop(0)

def isvalid(l):
    a, b = max(l)/1.1, min(l)/0.9
    if math.ceil(a) <= math.floor(b):
        return True
    return False

def ratatouille(matrix, resource, x, y):
    for i in range(x):
        for j in range(y):
            matrix[i][j] = matrix[i][j] / resource[i]
    for i in range(x):
        matrix[i] = sorted(matrix[i])
    pos = [0]*x
    res = 0
    while max(pos) < y:
        cur = []
        for i in range(x):
            cur += [matrix[i][pos[i]]]
        min_index = min(enumerate(cur), key=itemgetter(1))[0]
        if isvalid(cur):
            res += 1
            for i in range(x):
                pos[i] += 1
        else:
            pos[min_index] += 1
    return str(res)

f = open('C:/Users/Wilson/Desktop/Codejam 2017/R1_A/ratatouille/large_output.txt', 'w')

case = 1
while data:
    x, y = data[0][0], data[0][1]
    resource = data[1]
    matrix = data[2:2+x]
    f.write('Case #' + str(case) + ': ' + ratatouille(matrix, resource, x, y) + '\n')
    
    data = data[2+x:]
    case += 1

f.close()
