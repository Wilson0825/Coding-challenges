# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 23:52:21 2017

@author: Wilson
"""


data = []
with open("C:/Users/Wilson/Desktop/Codejam 2016/R1_B/match/B-small-practice.in", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(str, line.split(' '))))

data.pop(0)

def match(x, y):
    l = len(x)
    flag = 0
    for i in range(l):
        if x[i] != '?' and y[i] != '?':
            if x[i] > y[i]:
                flag = 1
            elif x[i] < y[i]:
                flag = -1
            check = i
            break
    for i in range(l):
        if x[i] != '?' and y[i] == '?':
            y[i] = x[i]
        elif x[i] == '?' and y[i] != '?':
            x[i] = y[i]
        elif x[i] == y[i] == '?':
            if flag == 0 or i < check:
                x[i] = y[i] = '0'
            elif flag == 1:
                x[i], y[i] = '0', '9'
            elif flag == -1:
                x[i], y[i] = '9', '0'
    return ''.join(x) + ' ' + ''.join(y)

f = open('C:/Users/Wilson/Desktop/Codejam 2016/R1_B/match/small_output.txt', 'w')

case = 1
while data:
    x, y = list(data[0][0]), list(data[0][1])
    f.write('Case #' + str(case) + ': ' + match(x, y) + '\n')
    
    data = data[1:]
    case += 1

f.close()
