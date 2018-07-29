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
with open("C:/Users/Wilson/Desktop/Codejam 2017/R1_A/cake/A-large.in", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(str, line.split(' '))))

data.pop(0)

def cake(matrix, x, y):
    matrix = [list(item[0]) for item in matrix]
    start = ['?']*x
    for i in range(x):
        for j in range(y):
            if matrix[i][j] != '?' and start[i] == '?':
                start[i] = matrix[i][j]
    blank = []
    for i in range(x):
        if matrix[i] == ['?']*y:
            blank += [i]
            continue
        for j in range(y):
            if matrix[i][j] == '?':
                matrix[i][j] = start[i]
            else:
                start[i] = matrix[i][j]
    for i in range(x):
        if i not in blank:
            start_row = matrix[i]
            break
    for i in range(x):
        if matrix[i] == ['?']*y:
            matrix[i] = start_row
        else:
            start_row = matrix[i]
    res = '\n'.join([''.join(item) for item in matrix])
    return res
    
    

f = open('C:/Users/Wilson/Desktop/Codejam 2017/R1_A/cake/large_output.txt', 'w')

case = 1
while data:
    x, y = int(data[0][0]), int(data[0][1])
    matrix = data[1:x+1]
    f.write('Case #' + str(case) + ':\n' + cake(matrix, x, y) + '\n')
    
    data = data[x+1:]
    case += 1

f.close()
