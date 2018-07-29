# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 22:35:09 2017

@author: Wilson
"""

data = []
with open("C:/Users/Wilson/Desktop/Codejam 2016/R1_A/lastword/A-large-practice.in", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(str, line.split(' '))))

data.pop(0)

def lastword(s):
    res = s[0]
    for i in range(len(s)-1):
        if s[i+1] >= res[0]:
            res = s[i+1] + res
        else:
            res += s[i+1]
    return res


f = open('C:/Users/Wilson/Desktop/Codejam 2016/R1_A/lastword/large_output.txt', 'w')

case = 1
while data:
    s = data[0][0]
    f.write('Case #' + str(case) + ': ' + lastword(s) + '\n')
    
    data = data[1:]
    case += 1

f.close()
