# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 14:18:23 2022

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

primes = [x for x in range(1,100000) if is_prime(x) == True]
oddcomp = [x for x in range(9,100000) if primes.count(x) == 0 if x %2 == 1 ]

for x in oddcomp:
    d = 0
    for p in primes:
        if d == 1:
            break
        if p < x:
            for s in range(1, math.floor(math.sqrt(x))):
                if p + 2* s**2 == x:
                    d = 1
                    break
    if d == 0:
        break
print(x)
                    
            
    
                