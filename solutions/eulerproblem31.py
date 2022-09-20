# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 14:24:55 2022

@author: muell
"""

"""
code ist mega dumm....niemand sollte das so machen
"""

m = 0

for a in range(0,2):
    count= 200*(1-a)
    if count == 0:
        m+=1
        continue
    for b in range(0, (200*(1-a)) // 100 +1):
        count = 200 - 200*a - 100*b
        if count == 0:
            m+=1
            continue
        for c in range(0,(200 - 200*a - 100*b)//50 +1):
            count = 200 - 200*a - 100*b - 50*c
            if count == 0:
                m+=1
                continue
            for d in range(0,(200 - 200*a - 100*b-50*c)//20 +1):
                count = 200 - 200*a - 100*b - 50*c - 20*d
                if count == 0:
                    m+=1
                    continue
                for e in range(0,(200 - 200*a - 100*b-50*c-20*d)//10 +1):
                    count = 200 - 200*a - 100*b - 50*c - 20*d - 10*e
                    if count == 0:
                        m+=1
                        continue
                    for f in range(0,(200 - 200*a - 100*b-50*c-20*d-10*e)//5 +1):
                        count = 200 - 200*a - 100*b - 50*c - 20*d - 10*e- 5*f
                        if count == 0:
                            m+=1
                            continue
                        for g in range(0,(200 - 200*a - 100*b-50*c-20*d-10*e-5*f)//2 +1):
                            count = 200 - 200*a - 100*b - 50*c - 20*d - 10*e- 5*f-2*g
                            if count == 0:
                                m+=1
                                continue
                            for h in range(0,(200 - 200*a - 100*b-50*c-20*d-10*e-5*f-2*g) +1):
                                count = 200 - 200*a - 100*b - 50*c - 20*d - 10*e- 5*f-2*g -h
                                if count == 0:
                                    m+=1
                                    continue
print(m)