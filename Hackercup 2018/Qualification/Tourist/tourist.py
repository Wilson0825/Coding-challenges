# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:45:46 2017

@author: Wilson
"""

data = []
with open("C:/Users/Wilson/Desktop/Coding/Hackercup 2018/Qualification/Tourist/tourist.txt", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(str, line.split(' '))))

data.pop(0)

def tourist(n, k, v, places):
    res, ind = [], []
    for i in range(k*(v-1), k*v):
        ind += i%n,
    for i in sorted(ind):
        res += places[i],
    return ' '.join(res)

f = open("C:/Users/Wilson/Desktop/Coding/Hackercup 2018/Qualification/Tourist/tourist_output.txt", "w")

case = 1
while data:
    n, k, v = map(int, data[0])
    places = [data[i][0] for i in range(1, n+1)]
    f.write('Case #' + str(case) + ': ' + tourist(n, k, v, places) + '\n')
    
    data = data[n+1:]
    case += 1

f.close()
