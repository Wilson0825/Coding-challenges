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
with open("C:/Users/Wilson/Desktop/Codejam 2017/R1_B/neighbor/test.txt", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(int, line.split(' '))))

data.pop(0)

valid = dict()
valid["R"] = ["Y","G","B"]
valid["O"] = ["B"]
valid["Y"] = ["R","B","V"]
valid["G"] = ["R"]
valid["B"] = ["R","O","Y"]
valid["V"] = ["Y"]

def dfs(res, cur, pos, final):
    if pos == len(res) - 1:
        last = [x for x in cur if cur[x] > 0][0]
        if last in valid[res[pos-1]] and last in valid[res[0]]:
            res[pos] = last
            print("yes")
            print(res)
            final += [res]
            return 
    for i in cur:
        if cur[i] > 0:
            if i in valid[res[pos-1]]:
                res[pos] = i
                cur[i] -= 1
                pos += 1
                dfs(res, cur, pos, final)
                pos -= 1
                cur[i] += 1

def neighbor(N, R, O, Y, G, B, V):
    res = [0]*N
    final = []
    items = dict()
    items["R"] = R
    items["O"] = O
    items["Y"] = Y
    items["G"] = G
    items["B"] = B
    items["V"] = V
    if len(items) == 1:
        return items[0]
    start = [i for i in items if items[i] > 0]
    for i in start:
        res[0] = i
        items[i] -= 1
        dfs(res, items, 1, final)
        items[i] += 1
        if final:
            return final
    return ("IMPOSSIBLE")
    

f = open('C:/Users/Wilson/Desktop/Codejam 2017/R1_B/neighbor/small_output.txt', 'w')

case = 1
while data:
    N, R, O, Y, G, B, V = data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6]
    f.write('Case #' + str(case) + ': ' + neighbor(N, R, O, Y, G, B, V) + '\n')
    
    data = data[1:]
    case += 1

f.close()
