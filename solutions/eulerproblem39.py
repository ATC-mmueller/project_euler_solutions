# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 18:31:20 2022

@author: muell
"""

per = [0 for x in range(0,1000)]

for c in range(5,500):
    for b in range(1,c):
        for a in range(b,c):
            if a**2 + b**2 == c**2:
                p = a+b+c
                if p <= 1000:
                    per[p-1] += 1
                    
m = 0 #maximal number of combinations
i = 0 # index/perimeter for max comb
for k in range(0,1000):
    if per[k] > m:
        m = per[k]
        i = k+1
print((m,i))
    