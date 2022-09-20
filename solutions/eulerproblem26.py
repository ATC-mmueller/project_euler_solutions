# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:17:26 2022

@author: muell
"""

c = 0 # length of the longest recurring cycle

for d in range(2,1000):
    j = 1 # counter for cycle
    while d%2 == 0:
        d = d//2
    while d % 5 == 0:
        d = d // 5
    if d==1:
        continue
    r = 10 % d # remainder of division
    while  r != 1:
        r = (r * 10) % d
        j += 1
    if j > c:
        n = d
        c = j
print(c)
print(n)
        
    