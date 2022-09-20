# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:38:41 2022

@author: muell
"""

pascal = [[1], [1,1]]
c = 0 #counter for exceeding 1.000.000
for n in range(2,101):
    pascal.append([1])
    for i in range(1,n):
        pascal[n].append(pascal[n-1][i-1] + pascal[n-1][i])
        if pascal[n][i] > 1000000:
            c += 1
    pascal[n].append(1)

print(c)