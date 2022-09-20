# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:12:40 2022

@author: muell
"""
digitdivs = []
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            if c*(10*a+b) == a*(10*b+c):
                digitdivs.append((10*a+b, 10*b+c))
print(digitdivs)
                