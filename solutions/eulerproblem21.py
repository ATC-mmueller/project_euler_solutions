# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 11:13:20 2022

@author: muell
"""
import math

amic = []
s = 0
for a in range(1,1000):
    div = []
    for i in range(1,math.ceil(a/2)+1):
        if a % i == 0:
            div.append(i)
    amic.append([a,sum(div)])
for m in amic: 
    for n in amic:
        if m[0] != n[0]:
            if m[0] == n[1] and m[1] == n[0]:
                s += m[0]
print(s)
    
    