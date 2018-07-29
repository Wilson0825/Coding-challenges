# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:45:46 2017

@author: Wilson
"""

data = []
with open("C:/Users/Wilson/Desktop/Coding/Hackercup 2018/Qualification/Interception/interception.txt", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(int, line.split(' '))))

data.pop(0)

def intercept(n):
    return '1\n0' if n%2 == 1 else '0'

f = open("C:/Users/Wilson/Desktop/Coding/Hackercup 2018/Qualification/Interception/interception_output.txt", "w")

case = 1
while data:
    n = data[0][0]
    f.write('Case #' + str(case) + ': ' + intercept(n) + '\n')
    
    data = data[n+2:]
    case += 1

f.close()
