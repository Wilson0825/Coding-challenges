# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 15:43:49 2018

@author: Wilson
"""
import sys
sys.setrecursionlimit(2000)

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

data = []
with open("C:/Users/Wilson/Desktop/Coding/Hackercup 2018/R1/traverse/ethan_traverses_a_tree.txt", "r") as f:
    for line in f:
        line = line.strip('\n')
        data.append(list(map(int, line.split(' '))))

data.pop(0)

def build_tree(nodes):
    root = Node(1)
    visit = [root]
    while visit:
        cur = visit.pop()
        left = nodes[cur.val-1][0]
        right = nodes[cur.val-1][1]
        if left != 0:
            cur.left = Node(left)
            visit += cur.left,
        if right != 0:
            cur.right = Node(right)
            visit += cur.right,
    return(root)

def preorder(root, res):
    if root is not None:
        res += root.val,
        preorder(root.left, res)
        preorder(root.right, res)

def postorder(root, res):
    if root is not None:
        postorder(root.left, res)
        postorder(root.right, res)
        res += root.val,

class unionfindset(object): 
    def __init__(self, n):
        self.id_ = list(range(n)) 
        self.size = [1]*n

    def root(self, i):
        j = i
        while j != self.id_[j]:
            self.id_[j] = self.id_[self.id_[j]]
            j = self.id_[j]
        return j
    
    def union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        if self.size[root_x] > self.size[root_y]:
            self.size[root_x] += self.size[root_y]
            self.id_[root_y] = root_x
        else:
            self.size[root_y] += self.size[root_x]
            self.id_[root_x] = root_y
    
    def find(self, x, y):
        return self.root(x) == self.root(y)

def traverse(n, k, tree):
    pre, post = [], []
    preorder(tree, pre)
    postorder(tree, post)
    
    ufset = unionfindset(n)
    for x in range(len(pre)):
        ufset.union(pre[x] - 1, post[x] - 1)
    
    res = []
    for x in range(len(pre)):
        res += ufset.root(x),
    
    if len(set(res)) < k:
        return 'Impossible'
    
    t = 1
    for i in set(res):
        res = [x if x != i else str(t) for x in res]
        t = t+1 if t < k else k
    
    return ' '.join(res)
    
f = open("C:/Users/Wilson/Desktop/Coding/Hackercup 2018/R1/traverse/traverse_output.txt", "w")

case = 1
while data:
    n, k = data[0][0], data[0][1]
    nodes = data[1:n+1]
    tree = build_tree(nodes)
    f.write('Case #' + str(case) + ': ' + traverse(n, k, tree) + '\n')
    
    data = data[n+1:]
    case += 1

f.close()
