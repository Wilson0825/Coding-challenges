# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 13:40:55 2018

@author: Wilson
"""

data = []
with open("C:/Users/Wilson/Desktop/Coding/Hackercup 2018/R1/let_it_flow/let_it_flow.txt", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(str, line.split(' '))))

data.pop(0)

def pipe(n, grid):
    if (n%2 == 1) or (grid[0][0] == '#') or (grid[2][n-1] == '#') or ('#' in grid[1]):
        return 0
    penalty = 0
    for i in range(1, n-1, 2):
        if '#' in grid[0][i:i+2] and '#' in grid[2][i:i+2]:
            return 0
        elif '#' in grid[0][i:i+2] or '#' in grid[2][i:i+2]:
            penalty += 1
    return int((2**((n-2)/2 - penalty)%1000000007))

f = open('C:/Users/Wilson/Desktop/Coding/Hackercup 2018/R1/let_it_flow/let_it_flow_output.txt', 'w')

case = 1
while data:
    print(case)
    n = int(data[0][0])
    grid = [x[0] for x in data[1:4]]
    
    f.write('Case #' + str(case) + ': ' + str(pipe(n, grid)) + '\n')
    
    data = data[4:]
    case += 1

f.close()