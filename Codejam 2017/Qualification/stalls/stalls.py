# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:42:27 2017

@author: Wilson
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 08:28:56 2017

@author: Wilson
"""
import collections

data = []
with open("C:/Users/Wilson/Desktop/Codejam 2017/Qualification/stalls/C-large.in", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(int, line.split(' '))))

data.pop(0)

def sep(x, rep, repo):
    if x%2 == 1:
        res = [(x-1)//2, (x-1)//2]
    else:
        res = [x//2, x//2 - 1]
    for item in res:
        if item not in repo:
            repo[item] = rep
        else:
            repo[item] += rep
    return res

def stalls(n, k):
    repo = collections.defaultdict(int)
    repo[n] = 1
    while k > 0:
        n = max(repo)
        rep = repo[n]
        repo.pop(n)
        cur = sep(n, rep, repo)
        k -= rep
    return cur


f = open('C:/Users/Wilson/Desktop/Codejam 2017/Qualification/stalls/large_output.txt', 'w')

case = 1
while data:
    n, k = data[0][0], data[0][1]
    f.write('Case #' + str(case) + ': ' + ' '.join(str(i) for i in stalls(n, k)) + '\n')
    
    data = data[1:]
    case += 1

f.close()
