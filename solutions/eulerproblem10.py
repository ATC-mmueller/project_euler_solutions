# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 15:35:11 2022

@author: muell
"""

import eulerproblem7
s = 0
for k in range(2,2000000):
    if eulerproblem7.isPrime(k) == 1:
        s += k
print(s)