# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:45:46 2017

@author: Wilson
"""

data = []
with open("C:/Users/Wilson/Desktop/Codejam/A-large.in", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(str, line.split(' '))))

data.pop(0)
        
def flip(x):
    for i in range(len(x)):
        if x[i] == '+':
            x[i] = '-'
        else:
            x[i] = '+'
    return x

def pancake(s, k):
    s = list(s)
    k = int(k)
    if '-' not in s:
        return 0
    if len(s) < k:
        return 'IMPOSSIBLE'
    step = 0
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            s[i:i+k] = flip(s[i:i+k])
            step += 1
    if '-' in s:
        return 'IMPOSSIBLE'
    return step

f = open('C:/Users/Wilson/Desktop/Codejam/large_output.txt', 'w')

case = 1
while data:
    s, k = data[0][0], data[0][1]
    f.write('Case #' + str(case) + ': ' + str(pancake(s, k)) + '\n')
    
    data = data[1:]
    case += 1

f.close()
