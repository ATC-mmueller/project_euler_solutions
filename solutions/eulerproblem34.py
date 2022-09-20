# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:30:49 2022

@author: muell
"""

def getNumberAsList(n):
    L=[]
    while n:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

def fact(n):
    p = n
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        for k in range(1,n):
            p = p*k
        return p
        

sof = 0

for a in range(3,1000000):
    L= getNumberAsList(a)
    s = 0
    for k in range(0,len(L)):
        s += fact(L[k])
    if s == a:
        sof += a
print(sof)