# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:11:04 2022

@author: muell
"""

def getNumberasList(n):
    L=[]
    while n>0:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

zifa = [x for x in range(1,10)]
zif = [x for x in range(0,10)]
pan = []

for a in zifa:
    for b in zif:
        if b not in {a}:
            for c in zif:
                if c not in {a,b}:
                    for d in zif:
                        if d not in {a,b,c}:
                            for e in zif:
                                if e not in {a,b,c,d}:
                                    for f in zif:
                                        if f not in {a,b,c,d,e}:
                                            for g in zif:
                                                if g not in {a,b,c,d,e,f}:
                                                    for h in zif:
                                                        if h not in {a,b,c,d,e,f,g}:
                                                            for i in zif:
                                                                if i not in {a,b,c,d,e,f,g,h}:
                                                                    for j in zif:
                                                                        if j not in {a,b,c,d,e,f,g,h,i}:
                                                                            p = a*10**9 + b*10**8 + c*10**7+d*10**6+e*10**5+f*10**4+g*10**3+h*10**2+i*10 + j
                                                                            pan.append(p)

prop = []
for p in pan:
    L = getNumberasList(p)
    if (100*L[1] + 10*L[2]+L[3]) % 2 == 0:
        if (100*L[2] + 10*L[3]+L[4]) % 3 == 0:
            if (100*L[3] + 10*L[4]+L[5]) % 5 == 0:
                if (100*L[4] + 10*L[5]+L[6]) % 7 == 0:
                    if (100*L[5] + 10*L[6]+L[7]) % 11 == 0:
                        if (100*L[6] + 10*L[7]+L[8]) % 13 == 0:
                            if (100*L[7] + 10*L[8]+L[9]) % 17 == 0:
                                prop.append(p)
print(sum(prop))
    