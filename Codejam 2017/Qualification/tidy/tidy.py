# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 23:00:06 2017

@author: Wilson
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:45:46 2017

@author: Wilson
"""

data = []
with open("C:/Users/Wilson/Desktop/Codejam/B-large.in", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(int, line)))

data.pop(0)
        
def check(x):
    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            return False
    return True

def tidy(n):
    if check(n):
        res = int(''.join(str(i) for i in n))
        return res
    cur = -1
    while not check(n):
        n[cur] = 9
        n[cur - 1] = n[cur - 1] - 1
        cur -= 1
    res = int(''.join(str(i) for i in n))
    return res

f = open('C:/Users/Wilson/Desktop/Codejam/large_output.txt', 'w')

case = 1
while data:
    n = data[0]
    f.write('Case #' + str(case) + ': ' + str(tidy(n)) + '\n')
    
    data = data[1:]
    case += 1

f.close()
