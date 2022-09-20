# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:55:12 2022

@author: muell
"""
chain = [0,0]
for n in range(2,500000):
    m = 2*n+1
    print(m)
    j=1
    while m != 1:
        if m % 2 == 0:
            m = m//2
            j +=1
        else:
            m = 3*m+1
            j +=1
    if j > chain[1]:
        chain = [2*n+1,j]
print(chain)
