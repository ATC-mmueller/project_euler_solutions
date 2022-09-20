# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:57:54 2022

@author: muell
"""
import math
abNum = []
for a in range(10,28123):
    if abNum.count(a) > 0:
        continue
    s= 1
    sq = math.sqrt(a)
    for i in range(2,math.ceil(sq)):
        if a % i == 0:
            s += (i+ a//i)
    if sq - math.floor(sq) == 0.0:
        s+= sq
    if s > a:
        for j in range(1,28123//a+1):
            if abNum.count(j*a) == 0:
                abNum.append(j*a)
abNum.sort()
#print(len(abNum))

nonSAbNum = [i for i in range(0,28123)]
for k in range(0,len(abNum)):
    l=k
    while l < len(abNum):
        s = abNum[k]+abNum[l]
        if s > 28123:
            break
        while s <= 28123:
            if nonSAbNum.count(s) >0:
                nonSAbNum.remove(s)
            s += abNum[l]
        l+=1
 #   print(k)
c = sum(nonSAbNum)
print(c)