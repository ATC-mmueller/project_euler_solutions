# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:35:36 2022

@author: muell
"""

def ten_digit_self_power(n):
    p = n
    for i in range(1,n):
        p *= n
    return p

s = 0
for i in range(1,1001):
    s += ten_digit_self_power(i)

print(s)