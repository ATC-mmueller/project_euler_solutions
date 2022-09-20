# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:10:02 2022

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

primes = [x for x in range(1,20000) if is_prime(x) == True]
c = 0 #counter for prime chain
p = 0
for i in range(21, len(primes)): #number of consecutive primes
    #sum of consecutive primes
    for j in range(0, len(primes)-i): #starting prime
        s = 0
        for k in range(0,i):
            s += primes[j+k]
        if s < 10**6:
            if is_prime(s) == True:
                p = s
                c = i
                print((p,c))