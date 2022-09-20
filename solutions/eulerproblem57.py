# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:38:33 2022

@author: muell
"""

def num_to_list(n):
    L=[]
    while n:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

L = [(1,1), (3,2)]

for k in range(2,1000):
    L.append((2*L[k-1][1]+L[k-1][0],2*L[k-1][1]+L[k-2][1]))

c = 0
for i in range(1000):
    if len(num_to_list(L[i][0])) > len(num_to_list(L[i][1])):
        c += 1
print(c)