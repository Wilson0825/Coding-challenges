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


data = []
with open("C:/Users/Wilson/Desktop/Codejam 2017/R1_B/steed/A-large.in", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(int, line.split(' '))))

data.pop(0)

def cruise(D, horses):
    cost = []
    for i in range(len(horses)):
        cost += [(D - horses[i][0])/horses[i][1]]
    return str(D/max(cost))

f = open('C:/Users/Wilson/Desktop/Codejam 2017/R1_B/steed/large_output.txt', 'w')

case = 1
while data:
    D, N = data[0][0], data[0][1]
    horses = data[1:N+1]
    f.write('Case #' + str(case) + ': ' + cruise(D, horses) + '\n')
    
    data = data[N+1:]
    case += 1

f.close()
