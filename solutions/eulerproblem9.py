# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 14:16:59 2022

@author: muell
"""
import math 

for b in range(1, 1000):
    for a in range(1, b):
        c2 = a**2 + b**2
        if  math.sqrt(c2)-math.floor(math.sqrt(c2)) == 0.0:
           c= math.sqrt(c2) 
           if a+b+c == 1000:
               print(a*b*c)