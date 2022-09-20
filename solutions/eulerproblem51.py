# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:11:37 2022

@author: muell
"""
import math 

def getNumberAsList(n):
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

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n == 4: 
        return False
    for m in range(2,math.ceil(math.sqrt(n))+1):
        if n % m == 0:
            return False
    return True

c = 0 #prime family counter
p = 0 #smallest prime in family

primes = [x for x in range(1,1000000) if is_prime(x) == True]
print(len(primes))
"""
primeslist = []
for p in primes:
    L = getNumberAsList(p)
    primeslist.append(L)
print(len(primeslist))
"""
"""
primes2 = []
for p in primes:
    L = getNumberAsList(p)
    for i in range(0,len(L)):
        for j in range(i+1,len(L)):
            if L[j] == L[i]:
                primes2.append((L,i,j))
"""
primes3 = []
for p in primes:
    L = getNumberAsList(p)
    for i in range(0,len(L)):
        for j in range(i+1,len(L)):
            for k in range(j+1, len(L)):
                if L[i] == L[j] == L[k]:
                    primes3.append((L,i,j,k))
print(len(primes3))
"""
primes4 = []
for (L,i,j,k) in primes3:
    for l in range(k+1,len(L)):
        if L[l] == L[i]:
            primes4.append((L,i,j,k,l))
print(len(primes4))

for (L,i,j) in primes2:
    c = 0
    n = 0
    P = L
    for k in range(0,10):
        P[i] = k
        P[j] = k
        if (P,i,j) in primes2:
            c += 1
        else:
            n += 1
        if n == 3:
            continue
    if c == 8:
        print(L)
        break
"""
eight = []
for (L,i,j,k) in primes3:
    c = 0
    n = 0
    P = []
    for v in range(0,len(L)):
        P.append(L[v])
    for l in range(0,10):
        P[i] = l
        P[j] = l
        P[k] = l
        if (P,i,j,k) in primes3:
            c += 1
        else:
            n += 1
        if n == 3:
            continue
    if c >= 8:
        m = list_to_num(L)
        if eight.count(m) == 0:
            eight.append(m)
eight.sort()
if len(eight)>0:
    print(eight[0])
        

""" note that a family of eight digit replacement primes 
can not be found in primes2.
Since going through the algorithm would increase the
digit sum by 2 every time, at least 3 numbers of that
family will be divisible by 3

with the same argumentation primes4 will also be out of question
Thus we can only find a solution in primesk with k= 3*n,
n natural number
"""