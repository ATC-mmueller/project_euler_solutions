# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:23:28 2022

@author: muell
"""

a, b = 1, 1 #numbers for Fibonacci
k, l = 1, 0 # Index k and length of number l

while l < 1000:
    a, b = b, a+b
    k += 1
    n = a
    l = 0
    while n > 0:
        n = n//10
        l += 1
print(k)