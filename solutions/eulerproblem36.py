# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 17:47:49 2022

@author: muell
"""

def getNumberasList(n):
    L=[]
    while n>0:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

def base2(n):
    L = []
    s= 0
    while n:
        L.append(n%2)
        n //= 2
    for k in range(0,len(L)):
        s += 10**k* L[k]
    return s


def is_palindrome(n):
    L = getNumberasList(n)
    for k in range(0,len(L)):
        if L[k] != L[len(L)-1-k]:
            return False
    return True

s=0
for l in range(1,1000000):
    if is_palindrome(l) == True:
        if is_palindrome(base2(l)) == True:
            s += l
print(s)     