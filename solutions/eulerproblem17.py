# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:47:07 2022

@author: muell
"""
def getNumberAsList(n):
    L=[]
    while n:
        L.append(n%10)
        n//=10
    L.reverse()
    return(L)

def letter(n):
    number = getNumberAsList(n)
    l = 0
    if len(number) == 4:
        l += 11
        return l
    if len(number) == 3:
        if number[0] == 1 or number[0] == 2 or number[0] == 6:
            l += 13
            number.remove(number[0])
        elif number[0] == 4 or number[0] == 5 or number[0] == 9:
            l += 14
            number.remove(number[0])
        elif number[0] == 3 or number[0] == 7 or number[0] == 8:
            l += 15
            number.remove(number[0])
    if len(number) == 2:
        if number[0] == 0:
            number.remove(number[0])
        elif number[0] == 1:
            if number[1] == 0:
                l += 3
                return l
            if number[1] == 1 or number[1] == 2:
                l += 6
                return l
            if number[1] == 5 or number[1] == 6:
                l += 7
                return l
            if number[1] == 3 or number[1] == 4 or number[1] == 8 or number[1] == 9:
                l += 8
                return l
            if number[1] == 7:
                l+= 9
                return l
        elif number[0] == 4:
            l += 5
            number.remove(number[0])
        elif number[0] == 2 or number[0] == 3 or number[0] ==8 or number[0] ==9:
            l += 6
            number.remove(number[0])
        elif number[0] == 5 or number[0] == 6:
            l+= 5
            number.remove(number[0])
        elif number[0] == 7:
            l += 7
            number.remove(number[0])
    if len(number) ==1:
        if number[0] == 0:
            return l
        elif number[0] == 1 or number[0] == 2 or number[0] == 6:
            l += 3
            return l
        elif number[0] == 4 or number[0] == 5 or number[0] == 9:
            l += 4
            return l
        elif number[0] == 3 or number[0] == 7 or number[0] == 8:
            l += 5
            return l
        
zahlen = list(range(1,1001))
buchstaben = [letter(x) for x in zahlen]
print(sum(buchstaben))

"""
code ist falsch. Es müssen noch die Ausnahmefälle für 100, 200, ... , 900
behandelt werden
"""