# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 18:31:20 2022

@author: muell
"""

import math

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

def trunc_right(p):
    while p >0:
        if is_prime(p) == True:
            p //= 10
        else:
            return False
    return True

def trunc_left(p):
    while p > 0:
        if is_prime(p) == True:
            L = getNumberasList(p)
            L.remove(L[0])
            if len(L) == 0:
                p = 0
            else:
                p = getNumberfromList(L)
        else:
            return False
    return True

trunc = []    
c = 0 #count truncable primes
k = 11

while c < 11:
    if trunc_left(k) == True:
        if trunc_right(k) == True:
            trunc.append(k)
            c += 1
    k += 1
    
print(trunc)
print(sum(trunc))