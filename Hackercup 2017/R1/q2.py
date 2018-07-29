# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 01:12:09 2017

@author: Wilson
"""

import collections

data = []
with open("C:/Users/Wilson/Desktop/fighting_the_zombies.txt", "r") as f:
    for line in f:
        data.append(list(map(int, line.split(' '))))
        
data.pop(0)

def right_bottom(z1, z2, r):
    if z2[0] - z1[0] <= r and z2[0] >= z1[0] and z1[1] - z2[1] <= r and z1[1] >= z2[1]:
        return True
    return False

def left_bottom(z1, z2, r):
    if z1[0] - z2[0] <= r and z1[0] >= z2[0] and z1[1] - z2[1] <= r and z1[1] >= z2[1]:
        return True
    return False

def fight(zombie, spell_range):
    dict1 = collections.defaultdict()
    dict2 = collections.defaultdict()
    
    for i in range(len(zombie)):
        z1 = zombie[i]
        right, left = [], []
        for j in range(len(zombie)):
            z2 = zombie[j]
            if right_bottom(z1, z2, spell_range):
                right += j,
            if left_bottom(z1, z2, spell_range):
                left += j,
        dict1[i] = right
        dict2[i] = left
    max_z = 0
    for i in range(len(zombie)):
        for j in range(i, len(zombie)):
            rr = len(set(dict1[i] + dict1[j]))
            lr = len(set(dict2[i] + dict1[j]))
            rl = len(set(dict1[i] + dict2[j]))
            ll = len(set(dict2[i] + dict2[j]))
            max_z = max(rr, lr, rl, ll, max_z)
    return max_z

f = open('C:/Users/Wilson/Desktop/fighting_the_zombies_output.txt', 'w')

case = 1
while data:
    n_zombie, spell_range = data[0][0], data[0][1]
    zombie = data[1:n_zombie+1]

    f.write('Case #' + str(case) + ': ' + str(fight(zombie, spell_range)) + '\n')
    
    data = data[n_zombie+1:]
    case += 1

f.close()
