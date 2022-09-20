# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 19:14:05 2022

@author: muell
"""

def getNumberasList(n):
    L=[]
    while n>0:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

def getNumberfromList(L):
    s = 0
    for k in range(0,len(L)):
        s+= 10**k * L[len(L)-1-k]
    return s

def is_pan19(n):
    L = getNumberasList(n)
    if L.count(0) > 0:
        return False
    for k in range(1,10):
        if L.count(k) == 1:
            L.remove(k)
        else:
            return False
    return True

pan = []

for n in range(9000,10000):
    L = getNumberasList(n)
    L1 = getNumberasList(2*n)
    for k in range(0,5):
        L.append(L1[k])
    p = getNumberfromList(L)
    if is_pan19(p) == True:
        pan.append(p)
print(pan)
    