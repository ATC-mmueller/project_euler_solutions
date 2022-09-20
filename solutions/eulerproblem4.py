# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 11:35:34 2022

@author: muell
"""
def getNumberAsList(n):
    L=[]
    while n:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

threedigit= [i for i in range(800,1000)]
threedigit.reverse()

for x in threedigit:
    for y in threedigit:
         a = getNumberAsList(x*y)
         i=0
         while i < len(a):
             if a[i] == a[len(a)-1-i]:
                 i = i+1
             elif a[i] != a[len(a)-1-i]:
                 break
             if i == len(a):
                 pal = x*y
         if i == len(a):
            break
    if i == len(a):
        break
print(pal)    
         