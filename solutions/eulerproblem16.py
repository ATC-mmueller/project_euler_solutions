# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:45:03 2022

@author: muell
"""

def getNumberAsList(n):
    L=[]
    while n:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

def quersumme(n):
    s = getNumberAsList(n)
    return(sum(s))