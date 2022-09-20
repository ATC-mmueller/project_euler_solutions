# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:46:22 2022

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

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n == 4: 
        return False
    for m in range(2,math.ceil(math.sqrt(n))+1):
        if n % m == 0:
            return False
    return True

def is_permutation(L):
    for i in range(0,4):
        if L[1].count(L[0][i]) >0:
            L[1].remove(L[0][i])
        else:
            return False
        if L[2].count(L[0][i]) >0:
            L[2].remove(L[0][i]) 
        else:
            return False
    return True
        

for i in range(1000, 3340):
    if is_prime(i) == True:
        L = [getNumberAsList(i), getNumberAsList(i+3330), getNumberAsList(i+6660)]
        if is_permutation(L) == True:
            print(L[0])