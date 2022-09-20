# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 09:31:07 2022

@author: muell
"""
import math

n=1
s=2
j=2
while n>0:
    j=2
    for m in range(2, math.floor(math.sqrt(n))):
        if n % m==0:
            j +=2
    if math.sqrt(n) - math.floor(math.sqrt(n)) == 0:
        j +=1
    if j > 500:
        print(n, " hat ", j, " Teiler")
        break
    n = n+s
    s += 1
