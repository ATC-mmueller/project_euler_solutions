# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:11:33 2022

@author: muell
"""
def pascal(n):
    if n == 0:
        return [1]
    elif n== 1:
        return [1,1]
    pas = [1,1]
    k = 1
    while k < n:
        j=1
        p = []
        p.append(1)
        while j <= k:
            p.append(pas[j-1]+pas[j])
            j +=1
        p.append(1)
        pas = p
        k +=1
    return(pas)

def routes(n):
    routes = [x**2 for x in pascal(n)]
    print("The number of lattice paths in a ", n, " times ", n, "-grid is ", sum(routes))
        
    
    
"""
pascal = [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
pascal2 = [x**2 for x in pascal]
print(sum(pascal2))
"""