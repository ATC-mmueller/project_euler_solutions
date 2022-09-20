# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 10:50:50 2022

@author: muell
"""
def fibsum(n):
    sum = 0
    a, b = 0, 1
    while a<n:
        a,b=b,a+b
        if a%2 == 0:
            sum = sum +a
    return(sum)
