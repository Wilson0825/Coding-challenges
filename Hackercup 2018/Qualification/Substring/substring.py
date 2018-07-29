# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:45:46 2017

@author: Wilson
"""

data = []
with open("C:/Users/Wilson/Desktop/Coding/Hackercup 2018/Qualification/Substring/ethan_searches_for_a_string.txt", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(str, line.split(' '))))

data.pop(0)

def findstr(s):
    start = ''
    for i in range(1, len(s)):
        if s[i] == s[0]:
            start += s[:i]
            break
    if not start:
        return 'Impossible'
    n = len(start)
    i = len(start)
    while i < len(s):
        temp = s[i:i+n]
        if temp not in start:
            return start + s
        i += n
    return 'Impossible'
    

f = open("C:/Users/Wilson/Desktop/Coding/Hackercup 2018/Qualification/Substring/ethan_searches_for_a_string_output.txt", "w")

case = 1
while data:
    s = data[0][0]
    f.write('Case #' + str(case) + ': ' + findstr(s) + '\n')
    
    data = data[1:]
    case += 1

f.close()
