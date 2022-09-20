# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:55:58 2022

@author: muell
"""

def word_to_number(name):
    number = 0
    for i in range(1,len(name)+1):
        if name[i-1] == 'A':
            number += 1
        if name[i-1] == 'B':
            number += 2
        if name[i-1] == 'C':
            number += 3
        if name[i-1] == 'D':
            number += 4
        if name[i-1] == 'E':
            number += 5
        if name[i-1] == 'F':
            number += 6
        if name[i-1] == 'G':
            number += 7
        if name[i-1] == 'H':
            number += 8
        if name[i-1] == 'I':
            number += 9
        if name[i-1] == 'J':
            number += 10
        if name[i-1] == 'K':
            number += 11
        if name[i-1] == 'L':
            number += 12
        if name[i-1] == 'M':
            number += 13
        if name[i-1] == 'N':
            number += 14
        if name[i-1] == 'O':
            number += 15
        if name[i-1] == 'P':
            number += 16
        if name[i-1] == 'Q':
            number += 17
        if name[i-1] == 'R':
            number += 18
        if name[i-1] == 'S':
            number += 19
        if name[i-1] == 'T':
            number += 20
        if name[i-1] == 'U':
            number += 21
        if name[i-1] == 'V':
            number += 22
        if name[i-1] == 'W':
            number += 23
        if name[i-1] == 'X':
            number += 24
        if name[i-1] == 'Y':
            number += 25
        if name[i-1] == 'Z':
            number += 26
    return number


my_file = open("p042_words.txt","r")
content = my_file.read()
content_list = content.split(',')
for k in range(0,len(content_list)):
    content_list[k] = content_list[k].strip('"')
my_file.close()


for k in range(0,len(content_list)):
    content_list[k] = word_to_number(content_list[k])

triangle = [x*(x+1)//2 for x in range(1,20)]

c = 0 #counter for triangle words
for k in range(0,len(content_list)):
    if triangle.count(content_list[k]) > 0:
        c += 1
print(c)