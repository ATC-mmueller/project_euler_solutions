# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 13:53:23 2022

@author: muell
"""

import math

i = 2 #index for triangle number
t = 3 #triangle number
tph = 0
while tph < 2:
    if (math.sqrt(24*t + 1) + 1) / 6 - math.floor((math.sqrt(24*t + 1) + 1) / 6) == 0.0:
        if (math.sqrt(8*t + 1) + 1) / 4 - math.floor((math.sqrt(8*t + 1) + 1) / 4) == 0.0:
            tph = tph + 1
            print(t)
    t += i+1
    i += 1
            