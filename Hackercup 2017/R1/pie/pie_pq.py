# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 09:53:18 2018

@author: Wilson Chu
"""
import heapq

data = []
with open("C:/Users/Wilson Chu/Desktop/pie_progress.txt", "r") as f:
    for line in f:
        data.append(list(map(int, line.split(' '))))
        
data.pop(0)

def min_cost(n_day, n_pie, cost):
    pie = []
    result = []
    for i in range(n_day):
        for j in range(n_pie):
            heapq.heappush(pie, cost[i][j])
        result += heapq.heappop(pie),
    return (sum(result))
        

f = open('C:/Users/Wilson Chu/Desktop/pie_progress_output.txt', 'w')

case = 1
while data:
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