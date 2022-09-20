# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 09:26:34 2022

@author: muell
"""
import math

# January 1st 1901 was a tuesday. Formula gives the first day of the following years.
def jan1(t):
    return (2 + t + math.floor(t/4) - math.floor(t/100) + math.floor(t/400)) % 7
# Create a list of all first days of the year
years = [jan1(t) for t in range(0,100)]

daysOfMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
months=[years]

feb = [(months[0][j-1]+31)%7 for j in range(1,101)]
months.append(feb)
months.append([])
for i in range(1,101):
    if i == 100:
        months[2].append((months[1][i-1] + 28)%7)
    elif i % 4 == 0:
        months[2].append((months[1][i-1] + 29)%7)
    else:
        months[2].append((months[1][i-1] + 28)%7)
for k in range(3,12):
    months.append([(months[k-1][j-1]+daysOfMonths[k-1])%7 for j in range(1,101)])
sundays = []
for l in range(0,12):
    s= months[l].count(0)
    sundays.append(s)
print(months)
print(sum(sundays))