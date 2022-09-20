# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 10:42:01 2022

@author: muell
"""
sum = 0
for x in range(1000):
    if x % 3 == 0:
        sum = sum+x
    if x % 5 == 0:
        sum= sum+x
    if x % 15 == 0:
        sum= sum-x
print(sum)
