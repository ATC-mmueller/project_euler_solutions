# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:40:44 2022

@author: muell
"""

import math

def is_prime(n):
    if n <= 0:
        return False
    if n == 2 or n == 3:
        return True
    if n == 4: 
        return False
    for m in range(2,math.ceil(math.sqrt(n))+1):
        if n % m == 0:
            return False
    return True

def getNumberAsList(n):
    L=[]
    while n:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

def getNumberfromList(L):
    s = 0
    for k in range(0,len(L)):
        s+= 10**k * L[len(L)-1-k]
    return s

primes = [x for x in range(2,1000000) if is_prime(x) == True]

def prime_rotation(p):
    P = getNumberAsList(p)
    if len(P) == 1:
        return True
    for l in range(0,len(P)):
        L= []
        for k in range(0,len(P)):
            L.append(P[k-l])
        if primes.count(getNumberfromList(L)) == 0:
            return False
    return True

circularPrimes = [p for p in primes if prime_rotation(p) == True]
print(len(circularPrimes))

"""     
P = [1,2,3,4,5]
for l in range(0,len(P)):
    L = []
    for k in range(0,len(P)):
        L.append(P[k-l])
    print(L)
"""