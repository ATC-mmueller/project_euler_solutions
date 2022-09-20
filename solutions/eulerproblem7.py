# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 13:26:38 2022

@author: muell
"""
import math

def isPrime(n):
    if n==2:
        return 1
    if n==3:
        return 1
    m=2
    while m <= math.floor(math.sqrt(n)):
        if n % m == 0:
            return 0
        m = m+1
        if m > math.floor(math.sqrt(n)):
            return 1

primes= []
i=2
k=0
while k<10001:
    if isPrime(i) ==1:
        primes.append(i)
        k = k+1
    i = i+1
print(primes[10000])

