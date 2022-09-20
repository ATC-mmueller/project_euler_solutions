# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:23:47 2022

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
    for i in range(0,len(L)):
        n += L[i]*(10**(len(L)-1-i))
    return n


def same_digits(n,m):
    N = num_to_list(n)
    M = num_to_list(m)
    if len(N) != len(M):
        return False
    for i in range(0,len(N)):
        if M.count(N[i]) == 0:
            return False
        else:
            M.remove(N[i])
    return True
    
        
for x in range(100000,200000):
    if same_digits(x,2*x) == True:
        if same_digits(x,3*x) == True:
            if same_digits(x,4*x) == True:
                if same_digits(x,5*x) == True:
                    if same_digits(x,6*x) == True:
                        print(x)
                        break