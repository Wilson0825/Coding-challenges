# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 09:35:26 2017

@author: Wilson
"""
data = []
with open("C:/Users/Wilson/Desktop/manic_moving.txt", "r") as f:
    for line in f:
        data.append(list(map(int, line.split(' '))))
        
data.pop(0)

max_int = 2<<30

def floyd(n_city, route):
    distance = [[max_int for _ in range(n_city)] for _ in range(n_city)]
    for i in range(len(distance)):
        distance[i][i] = 0
    for x in route:
        distance[x[0] - 1][x[1] - 1] = x[2]
        distance[x[1] - 1][x[0] - 1] = x[2]
    for k in range(len(distance)):
        for i in range(len(distance)):
            for j in range(len(distance)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance

def min_gas(family, distance):
    start = 0
    f = [[x[0]-1, x[1]-1] for x in family]
    for x in f:
        if distance[x[0]][x[1]] == max_int:
            return -1
    
    dp = [[0 for _ in range(len(f))] for _ in range(2)]
    dp[0][0] = distance[start][f[0][0]] + distance[f[0][0]][f[0][1]]
    if len(f) == 1:
        return dp[0][0]
    dp[1][0] = distance[start][f[0][0]] + distance[f[0][0]][f[1][0]] + distance[f[1][0]][f[0][1]]
    start = f[0][1]
    
    for i in range(1, len(f)):
        dp[0][i] = min(dp[0][i-1] + distance[start][f[i][0]] + distance[f[i][0]][f[i][1]],\
        dp[1][i-1] + distance[start][f[i][1]])
        if i+1 < len(f):
            dp[1][i] = min(dp[0][i-1] + distance[start][f[i][0]] + distance[f[i][0]][f[i+1][0]] + distance[f[i+1][0]][f[i][1]],\
            dp[1][i-1] + distance[start][f[i+1][0]] + distance[f[i+1][0]][f[i][1]])
        start = f[i][1]
    
    return dp[0][-1]

f = open('C:/Users/Wilson/Desktop/manic_moving_output.txt', 'w')

case = 1
while data:
    n_city, n_route, n_family = data[0][0], data[0][1], data[0][2]
    route = data[1:n_route+1]
    family = data[n_route+1:n_route+n_family+1]
    distance = floyd(n_city, route)
    
    f.write('Case #' + str(case) + ': ' + str(min_gas(family, distance)) + '\n')
    
    data = data[n_route+n_family+1:]
    case += 1

f.close()