# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 09:59:49 2022

@author: muell
"""

def is_pent(n):
    k = 1
    while k*(3*k-1)/2 <= n:
        if k*(3*k-1)/2 == n:
            return True
        k += 1
    return False

pent = [1,5,12,22]
d = 0
i = 4 # counts index of P_i
while d == 0:
    for k in range(1,len(pent)):
        if pent.count(pent[len(pent)-1]-pent[k]) >0:
            if is_pent(pent[k]+pent[len(pent)-1]) == True:
                d = pent[len(pent)-1]-pent[k]
                print((pent[len(pent)-1], pent[k], d))
    i += 1
    p = pent[len(pent)-1] + 3*i -2
    if pent.count(p) == 0:
        pent.append(p)
    if 3*i+1 > pent[0]:
        pent.remove(pent[0])
    if i % 100 == 0:
        print(i)