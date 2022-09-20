# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 10:56:54 2022

@author: muell
"""

def num_to_list(n):
    L=[]
    while n:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

def list_to_num(L):
    n = 0
    for l in range(len(L)):
        n += L[l] * (10**(len(L)-1-l))
    return n
        
def is_pal(n):
    L = num_to_list(n)
    for k in range(len(L)//2):
        if L[k] != L[len(L)-1-k]:
            return False
    return True

def rev(n):
    L = num_to_list(n)
    L.reverse()
    m = list_to_num(L)
    return m
    
c = 0 #coutner of Lychrel
for n in range(1,10000):
    l = n
    for k in range(55):
        l += rev(l)
        if is_pal(l) == True:
            break
    if k > 50:
        c += 1

print(c)
            
    
    