# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:52:21 2017

@author: Wilson
"""


data = []
with open("C:/Users/Wilson/Desktop/Codejam 2016/R1_A/soldier/B-large-practice.in", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(int, line.split(' '))))

data.pop(0)

def soldier(matrix):
    res = []
    for row in matrix:
        for item in row:
            if item not in res:
                res += [item]
            else:
                res.remove(item)
    return ' '.join(map(str, sorted(res)))


f = open('C:/Users/Wilson/Desktop/Codejam 2016/R1_A/soldier/large_output.txt', 'w')

case = 1
while data:
    s = data[0][0]
    matrix = data[1:2*s]
    f.write('Case #' + str(case) + ': ' + soldier(matrix) + '\n')
    
    data = data[2*s:]
    case += 1

f.close()
