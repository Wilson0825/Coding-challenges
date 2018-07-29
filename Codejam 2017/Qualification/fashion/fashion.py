# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 19:19:34 2017

@author: Wilson
"""

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

data = []
with open("C:/Users/Wilson/Desktop/Codejam/D-small-attempt0.in", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(str, line.split(' '))))

data.pop(0)

def check_row(matrix, row):
    this_row = [i for i in matrix[row] if i != '.' and i != '+']
    if len(this_row) >= 2:
        return False
    return True

def check_col(matrix, col):
    this_col = [i[col] for i in matrix if i[col] != '.' and i[col] != '+']
    if len(this_col) >= 2:
        return False
    return True

def check_diag(matrix, row, col):
    diag1 = []
    diag2 = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i - row == j - col and matrix[i][j] != '.' and matrix[i][j] != 'x':
                diag1 += [matrix[i][j]]
            if i - row == col - j and matrix[i][j] != '.' and matrix[i][j] != 'x':
                diag2 += [matrix[i][j]]
    if len(diag1) >= 2 or len(diag2) >= 2:
        return False
    return True

def fashion(matrix):
    nrow = len(matrix)
    res = []
    for i in range(nrow):
        for j in range(nrow):
            if matrix[i][j] != 'o':
                prev = matrix[i][j]
                matrix[i][j] = 'o'
                if check_row(matrix, i) and check_col(matrix, j) and check_diag(matrix, i, j):
                    res += [['o', str(i), str(j)]]
                else:
                    matrix[i][j] = prev
    for i in range(nrow):
        for j in range(nrow):
            if matrix[i][j] == '.':
                matrix[i][j] = '+'
                if check_row(matrix, i) and check_col(matrix, j) and check_diag(matrix, i, j):
                    res += [['+', str(i), str(j)]]
                    continue
                matrix[i][j] = 'x'
                if check_row(matrix, i) and check_col(matrix, j) and check_diag(matrix, i, j):
                    res += [['x', str(i), str(j)]]
                    continue
                matrix[i][j] = '.'
    score = 0
    for i in range(nrow):
        for j in range(nrow):
            if matrix[i][j] == 'x' or matrix[i][j] == '+':
                score += 1
            if matrix[i][j] == 'o':
                score += 2
    res = [[str(score), str(len(res))]] + res
    final = '\n'.join([' '.join(item) for item in res])
    return final
    

f = open('C:/Users/Wilson/Desktop/Codejam/small_output.txt', 'w')

case = 1
while data:
    n, m = int(data[0][0]), int(data[0][1])
    matrix = [['.' for i in range(n)] for j in range(n)]
    if m > 0:
        for i in range(m):
            row = int(data[i+1][1]) - 1
            col = int(data[i+1][2]) - 1
            matrix[row][col] = data[i+1][0]
    f.write('Case #' + str(case) + ': ' + fashion(matrix) + '\n')
    
    data = data[1+m:]
    case += 1

f.close()
