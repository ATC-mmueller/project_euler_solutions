# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:45:31 2022

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

L = [1]
k = 1 #layer counter
p = 0 #prime counter
while k:
    L.append((2*k+1)**2)
    for j in range(1,4):
        L.append((2*k+1)**2 -2*k*j)
        if is_prime((2*k+1)**2 -2*k*j) == True:
            p += 1
    if p / len(L) < 0.1:
        break
    k+=1
print(2*k+1)