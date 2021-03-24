# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:15:33 2021

@author: sajan
"""
import itertools
m=2
trans=[[0 for j in range (m)] for i in range(m)]
trans[0]=[0.99,0.01]
trans[1]=[0.2,0.8]
initial=[0.5,0.5]
k=6
emit=[[0 for j in range (k)] for i in range(m)]
emit[0]=[1.0/6 for j in range(k)]
emit[1]=[0.1 for j in range(k)]
emit[1][5]=0.5
eseq=6
# Enter the sequence with spaces between the numbers
line=input('What is the sequence of emmisions; no commmas: ')
seq=line.split()
eseq=[int(value) for value in seq]
n=len(seq)
possibilities_states=list(itertools.product([0, 1], repeat=n))
pmax =[]
for i in range(len(possibilities_states)):
    for j in range(n):
        if j==0:
            prob=0.5
            if possibilities_states[i][j] == 0:
                prob = prob*(1.0/6)
            else: 
                if eseq[j] == 6:
                    prob = prob*0.5
                else: 
                    prob = prob*0.1
        else:
            if possibilities_states[i][j-1] == 0 and possibilities_states [i][j] == 0:
                prob = prob * 0.99
                if possibilities_states[i][j] == 0:
                    prob = prob*(1.0/6)
                else: 
                    if eseq[j] == 6:
                        prob = prob*0.5
                    else: 
                        prob = prob*0.1
            elif possibilities_states[i][j-1] == 0 and possibilities_states [i][j] == 1:
                prob = prob*0.01
                if possibilities_states[i][j] == 0:
                    prob = prob*(1.0/6)
                else: 
                    if eseq[j] == 6:
                        prob = prob*0.5
                    else: 
                        prob = prob*0.1
            elif possibilities_states[i][j-1] == 1 and possibilities_states [i][j] == 0:
                prob = prob*0.2
                if possibilities_states[i][j] == 0:
                    prob = prob*(1.0/6)
                else: 
                    if eseq[j] == 6:
                        prob = prob*0.5
                    else: 
                        prob = prob*0.1 
            elif possibilities_states[i][j-1] == 1 and possibilities_states [i][j] == 1:
                prob = prob*0.8
                if possibilities_states[i][j] == 0:
                    prob = prob*(1.0/6)
                else: 
                    if eseq[j] == 6:
                        prob = prob*0.5
                    else: 
                        prob = prob*0.1
    pmax.append(prob)
print ('The highest probability recorded was:', max(pmax,key=lambda x:float(x)))
pmax1 = pmax[0]
sseq = possibilities_states[0]
sseq1 =[]
for x in range(len(pmax)):
    if pmax[x] > pmax1:
        pmax1 = pmax[x]
        sseq = possibilities_states[x]
for x in range(len(sseq)):
    if sseq[x] == 0:
        sseq1.append('F')
    else:
        sseq1.append('L')
print('The most probable scenario is: ', sseq, sseq1)

    
