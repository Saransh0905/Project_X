#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 01:01:09 2019

@author: saransh
"""

import pandas as pd
data = open("/home/saransh/Documents/Github/Project_X/organisedData/taenia_solium.PRJNA170813.WBPS14.protein.txt","r")
l = data.readlines()
seq = []
st = ''
for i in range(len(l)):
    if l[i][0]!='>':
        st = st+l[i][0:len(l[i])-1]
    else:
        seq.append(st)
        st = ''
out100 = open("/home/saransh/Documents/Github/Project_X/organisedData/out100_taenia_solium.txt","w")
ans  = []
for s in seq:
    if len(s)<=100:
        ans.append(s)
for i in range(len(ans)):
    out100.write(">"+ans[i])
    out100.write("\n")
ans = []
for s in seq:
    if len(s)<=100:
        for j in range(len(s)-1,0,-1):
            if s[j]+s[j-1] =='RK' or s[j]+s[j-1] =='KR' or s[j]+s[j-1] =='KK' or s[j]+s[j-1] =='RR':
                for k in range(j-1,0,-1):
                    if s[k]=="P" or s[k]=="Q":
                        ans.append(s[k:j+1])
                    
out = open("/home/saransh/Documents/Github/Project_X/organisedData/out_taenia_solium.txt","w")
for i in range(len(ans)):
    out.write(">"+ans[i])
    out.write("\n")
