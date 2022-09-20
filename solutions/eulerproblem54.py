# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 20:09:44 2022

@author: muell
"""

my_file = open("p054_poker.txt","r")
content = my_file.read()
content_list = content.split('\n')
my_file.close()
for k in range(1000):
    content_list[k] = content_list[k].split()

p1 = []
p2 = []
for k in range(1000):
    p1.append(content_list[k][:5])
    p2.append(content_list[k][5:])

def card_value(card):
    if card == '1':
        return 1
    if card == '2':
        return 2
    if card == '3':
        return 3
    if card == '4':
        return 4
    if card == '5':
        return 5
    if card == '6':
        return 6
    if card == '7':
        return 7
    if card == '8':
        return 8
    if card == '9':
        return 9
    if card == 'T':
        return 10
    if card == 'J':
        return 11
    if card == 'Q':
        return 12
    if card == 'K':
        return 13
    if card == 'A':
        return 14

""" idea: create a list out of every hand containing the hand values:
position 0: straight flush
1: four of a kind
2: full house
3: flush
4: straight
5: three of a kind
6: two pairs
7: one pair
8: high card  

if a hand satisfies criterion k, put the value of the highest card
fullfilling said criterion in L[k].
card values: 2-9 = 2-9
T = 10, J = 11, Q = 12, K = 13, A = 14

of course a hand can fulfill more than one criterion. 
for example: a royal flush is also a flush with high card ace 
and a straight with high card ace.

in the end, compare the lists of both players. At some point
the values L1[k] != L2[k] and we know who wins.
"""      



def hand_value(L):
    H = [0,0,0,0,0,0,0,0,0]
    high, pair, pair2, three, fullhouse, four = 0,0,0,0,0,0
    straight, flush, strflush = 0,0,0
    for k in range(5): #high card loop
        if card_value(L[k][0]) > high:
            high = card_value(L[k][0])
    for i in range(5): #pair loop
        for j in range(i+1,5):
            if card_value(L[i][0]) == card_value(L[j][0]):
                pair = card_value(L[i][0])
                for k in range(j+1,5):#three loop
                    if card_value(L[k][0]) == card_value(L[i][0]):
                        three = card_value(L[k][0])
                    if three >0:
                        for l in range(k+1,5): #four loop
                            if card_value(L[l][0]) == card_value(L[i][0]):
                                four = card_value(L[l][0])
                        for m in range(5):#fullhouse loop
                            if m not in {i,j,k}: 
                                for n in range(m+1,5):
                                    if n not in {i,j,k,m}:
                                        if card_value(L[m][0]) == card_value(L[n][0]):
                                            fullhouse = card_value(L[k][0])
                for m in range(5): #two pair loop
                    if m not in {i,j}:
                        for n in range(m+1,5):
                            if n not in {i,j,m}:
                                if card_value(L[m][0]) == card_value(L[n][0]):
                                    if card_value(L[j][0]) > card_value(L[m][0]):
                                        pair = card_value(L[j][0])
                                        pair2 = card_value(L[j][0])
                                    else: 
                                        pair = card_value(L[m][0])
                                        pair2 = card_value(L[m][0])
    for i in range(5): #straight loop
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    if card_value(L[i][0]) == high - 1:
                        if card_value(L[j][0]) == high - 2:
                            if card_value(L[k][0]) == high - 3:
                                if card_value(L[l][0]) == high - 4:
                                    straight = high
    if L[0][1] == L[1][1] == L[2][1] == L[3][1] == L[4][1]:
        flush = high
        if straight > 0:
            strflush = high
    H[0] = strflush
    H[1] = four
    H[2] = fullhouse
    H[3] = flush
    H[4] = straight
    H[5] = three
    H[6] = pair2
    H[7] = pair
    H[8] = high
    return H
    
c = 0 #counts how many times p1 wins
for n in range(1000):
    if hand_value(p1[n]) > hand_value(p2[n]):
        c += 1

print(c)
    
    
