# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:32:49 2022

@author: muell
"""

def num_to_list(n):
    L=[]
    while n:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

def dig_sum(n):
    L = num_to_list(n)
    s = 0
    for k in range(len(L)):
        s += L[k]
    return s

maxdigsum = 0

for a in range(100):
    for b in range(100):
        s = dig_sum(a**b)
        if s > maxdigsum:
            maxdigsum = s
print(maxdigsum)
        