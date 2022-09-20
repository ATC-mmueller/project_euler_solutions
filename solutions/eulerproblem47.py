# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 14:32:55 2022

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

primes = [x for x in range(1,200000) if is_prime(x) == True]
test = [x for x in range(100000,200000) if primes.count(x) == 0 if primes.count(x+1) == 0 if primes.count(x+2) == 0 if primes.count(x+3) == 0]
print(test)
f = 0 #counts prime factors

def fourprimes(n):
    f = 0
    if primes.count(n) == 1:
        return False
    for p in primes:
        if p < n+ 1:
            if n %p == 0:
                f += 1
                while n%p==0:
                    n //= p
        else:
            break
    if f == 4:
        return True
    return False

for x in test:
    if fourprimes(x) == True:
        if fourprimes(x+1) == True:
            if fourprimes(x+2) == True:
                if fourprimes(x+3) == True:
                    break
print(x)
            