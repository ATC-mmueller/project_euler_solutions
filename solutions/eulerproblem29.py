# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:48:03 2022

@author: muell
"""

dist = set()
for a in range(2,101):
    for b in range(2,101):
        dist.add(a**b)
print(len(dist))