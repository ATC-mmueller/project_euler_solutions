# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 11:03:29 2022

@author: muell
"""
import math

def getNumberAsList(n):
    L=[]
    while n:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

a= math.factorial(100)
L= getNumberAsList(a)
print(sum(L))
