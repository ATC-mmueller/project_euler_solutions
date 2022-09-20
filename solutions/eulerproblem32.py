# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:55:10 2022

@author: muell
"""

pan = list(range(1,10))
panprod = []

for a in pan:
    for b in pan:
        if b != a:
            for c in pan:
                if c not in {a,b}:
                   for d in pan:
                       if d not in {a,b,c}:
                          for e in pan:
                              if e not in {a,b,c,d}:
                                 for f in pan:
                                     if f not in {a,b,c,d,e}:
                                        for g in pan:
                                            if g not in {a,b,c,d,e,f}:
                                               for h in pan:
                                                   if h not in {a,b,c,d,e,f,g}:
                                                      for j in pan:
                                                          if j not in {a,b,c,d,e,f,g,h}:
                                                              m = 10*a+b
                                                              n = 100*c+10*d+e
                                                              p = 1000*f + 100*g + 10*h + j
                                                              if m * n == p:
                                                                  panprod.append(p)
                                                              if a* (1000*b+100*c+10*d+e) == p:
                                                                  panprod.append(p)
print(sum([x for x in set(panprod)]))