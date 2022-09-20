# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:57:53 2022

@author: muell
"""

s = 0 #sum of digit fifth powers

def getNumberAsList(n):
    L=[]
    while n:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

for n in range(2,300000):
    fifth = [x**5 for x in getNumberAsList(n)]
    if n == sum(fifth):
        s += n
print(s)