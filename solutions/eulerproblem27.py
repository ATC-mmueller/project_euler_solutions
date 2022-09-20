# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:16:32 2022

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
    for m in range(2,math.floor(math.sqrt(n))):
        if n % m == 0:
            return False
    return True

const = [n for n in range(2,1000) if is_prime(n) == True] # b has to be prime
coeff = [] # coefficients a, b in expression k**2 + ak + b
c = 0 # longest cycle of consecutive primes
for a in range(-999,1000):
    for b in const:
        k = 0
        j = 0
        while is_prime(k**2 + a*k + b) == True:
            k += 1
            j += 1
        if j > c:
            coeff = [a,b]
            c = j
print(coeff)
            