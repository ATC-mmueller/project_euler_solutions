# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:22:04 2022

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

""" 

note that a prime number can not be a 1 through 9 pandigital number.
Since a 1 through 9 pandigital number has digit sum 45, it is divisible by 3.
With the same argumentation a 1 through 8 pandigital number can not be prime.
Hence the highest pandigital prime can only be a 1 through 7 pan

""" 

zif = [8-x for x in range(1,8)]
pan = []

for c in zif:
    for d in zif:
        if d not in {c}:
            for e in zif:
                if e not in {c,d}:
                    for f in zif:
                        if f not in {c,d,e}:
                            for g in zif:
                                if g not in {c,d,e,f}:
                                    for h in zif:
                                        if h not in {c,d,e,f,g}:
                                            for i in zif:
                                                if i not in {c,d,e,f,g,h}:
                                                    p = c*10**6+d*10**5+e*10**4+f*10**3+g*10**2+h*10+i
                                                    if is_prime(p) == True:
                                                        pan.append(p)
print(pan[0])