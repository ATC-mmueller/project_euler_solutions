# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 10:58:08 2022

@author: muell
"""
import math
n = int(input("Please input integer for largest prime factor: "))
a= list(range(2,math.floor(math.sqrt(n))))
for x in a:
    if n % x == 0: # test if number divides n
        m=2
        while m < x: # test if divisor is prime
            if x % m ==0:
                break
            else: 
                m=m+1
                if m==x:
                    p=x
            
        
            


