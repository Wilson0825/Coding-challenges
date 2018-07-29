# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 10:20:11 2018

@author: Wilson
"""

data = []
with open("C:/Users/Wilson/Desktop/Coding/Codejam 2018/Qualification/Universe/test.txt", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(str, line.split(' '))))
        
data.pop(0)

def save_universe(target, program):
    cur_dmg = 0
    cur_power = 1
    for step in program:
        if step == 'C':
            cur_power *= 2
        elif step == 'S':
            cur_dmg += cur_power
    result = 0
    flag = 1
    while flag == 1 and cur_dmg > target:
        n_c = 1
        for i in range(len(program) - 1, 0, -1):
            if program[i] == 'C':
                n_c += 1
            elif program[i] == 'S' and program[i-1] == 'C':
                program[i], program[i-1] = program[i-1], program[i]
                result += 1
                cur_dmg -= cur_power >> n_c
                flag = 1
                break
            else:
                flag = 0
    if cur_dmg > target:
        return 'IMPOSSIBLE'
    return str(result)


f = open('C:/Users/Wilson/Desktop/Coding/Codejam 2018/Qualification/Universe/output.txt', 'w')

case = 1
while data:
    target, program = int(data[0][0]), list(data[0][1])
    f.write('Case #' + str(case) + ': ' + save_universe(target, program) + '\n')
    
    data = data[1:]
    case += 1

f.close()










# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 10:20:11 2018

@author: Wilson
"""

def save_universe(target, program):
    cur_dmg = 0
    cur_power = 1
    for step in program:
        if step == 'C':
            cur_power *= 2
        elif step == 'S':
            cur_dmg += cur_power
    result = 0
    flag = 1
    while flag == 1 and cur_dmg > target:
        n_c = 1
        for i in range(len(program) - 1, 0, -1):
            if program[i] == 'C':
                n_c += 1
            elif program[i] == 'S' and program[i-1] == 'C':
                program[i], program[i-1] = program[i-1], program[i]
                result += 1
                cur_dmg -= cur_power >> n_c
                flag = 1
                break
            else:
                flag = 0
    if cur_dmg > target:
        return 'IMPOSSIBLE'
    return result

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  m, n = [str(s) for s in input().split(" ")]
  target, program = int(m), list(n)
  print("Case #{}: {}".format(i, save_universe(target, program)))





