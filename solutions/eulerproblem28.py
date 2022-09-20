# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:38:26 2022

@author: muell
"""

spiral = 1
n = 1
while 2*n+1 <= 1001:
    k = 2*n +1
    spiral = spiral + (k**2 + 3 * (k**2 - 2*(k-1)))
    n += 1
print(spiral)