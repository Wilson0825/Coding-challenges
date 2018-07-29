# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 17:56:59 2017

@author: Wilson
"""


data = []
with open("C:/Users/Wilson/Desktop/Coding/Hackercup 2017/R1/pie/pie_progress.txt", "r") as f:
    for line in f:
        data.append(list(map(int, line.split(' '))))

data.pop(0)

def min_cost(n_day, n_pie, cost):
    result = [[0 for i in range(n_day)] for j in range(n_day+1)]
    result[n_day][0] = cost[n_day-1][0]
    for i in range(n_day-1, 0, -1):
        for j in range(n_day-i+1):
            temp = []
            if j == 0:
                for k in range(1, n_pie+1):
                    if j+k-1 <= n_day-1:
                        temp += sum(cost[i-1][:k]) + result[i+1][j+k-1],
            else:
                for k in range(n_pie+1):
                    if j+k-1 <= n_day-1:
                        temp += sum(cost[i-1][:k]) + result[i+1][j+k-1],
            result[i][j] = min(temp)
    return result[1][0]

f = open('C:/Users/Wilson/Desktop/Coding/Hackercup 2017/R1/pie/pie_progress_output.txt', 'w')

case = 1
while data:
    print(case)
    n_day, n_pie = data[0][0], data[0][1]
    matrix = [sorted(x) for x in data[1:n_day+1]]
    cost = []
    for i in range(n_day):
        temp = []
        for j in range(n_pie):
            temp += matrix[i][j] + (2*j+1),
        cost += [temp]
    
    if n_pie > n_day:
        n_pie = n_day
    
    f.write('Case #' + str(case) + ': ' + str(min_cost(n_day, n_pie, cost)) + '\n')
    
    data = data[n_day+1:]
    case += 1

f.close()
