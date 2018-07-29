# -*- coding: utf-8 -*-
"""
Created on Sat May  5 06:09:49 2018

@author: Wilson
"""

def newword(N, L, words):
    n_distinct = len(set([w[0][0] for w in words]))
    result = '-'
    i = 1
    while i < L:
        n_distinct *= len(set([w[0][i] for w in words]))
        if n_distinct > N:
            diction, pool = {}, set([w[0][:i+1] for w in words])
            for w in words:
                diction[w[0][:i]] = diction[w[0][:i]]+1 if w[0][:i] in diction else 1
            prefix = min(diction, key=diction.get)
            for w in words:
                if prefix + w[0][i] not in pool:
                    return prefix + w[0][i:]
        i += 1
    return result

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N, L = [int(s) for s in input().split(" ")]
    words = []
    for j in range(N):
        words += [str(s) for s in input().split(" ")],
    print("Case #{}: {}".format(i, newword(N, L, words)))
