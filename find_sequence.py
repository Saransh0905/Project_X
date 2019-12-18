#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 01:01:09 2019

@author: saransh
"""

import pandas as pd
from collections import Counter 


data = open("/home/saransh/Documents/Github/Project_X/organisedData/taenia_solium.PRJNA170813.WBPS14.protein.txt","r")
l = data.readlines()
seq = []
code = []
st = ''
for i in range(len(l)):
    if l[i][0]!='>':
        st = st+l[i][0:len(l[i])-1]
    else:
        code.append(l[i][0:len(l[i])-1])
        seq.append(st)
        st = ''
seq.append(st)
seq.remove('')
'''
out100 = open("/home/saransh/Documents/Github/Project_X/organisedData/sequence_with_length_than100.txt","w")
ans  = []

for s in seq:
    if len(s)<=100:
        ans.append(s)
for i in range(len(ans)):
    out100.write(">"+ans[i])
    out100.write("\n")
'''
ans = []

numbering = []
count = -1
for s in seq:
    count+=1
    j = len(s)-1
    while j!=0:
        if s[j]+s[j-1] =='RK' or s[j]+s[j-1] =='KR' or s[j]+s[j-1] =='KK' or s[j]+s[j-1] =='RR':
            for k in range(j-1,0,-1):
                if s[k]=="P" or s[k]=="Q":
                    ans.append(s[k:j+1])
                    numbering.append(count)
                    j = k
                    break
        j-=1
'''                    
out = open("/home/saransh/Documents/Github/Project_X/organisedData/found_RK.txt","w")
for i in range(len(seq)):
    #ind = 1
    if numbering.count(i)>0:
        out.write(code[i] + " Total =  "+str(numbering.count(i)))
        out.write("\n")
        for j in range(len(ans)):
            if numbering[j]==i:
                #out.write(str(ind)+". ")
                out.write(">"+ans[j])
                out.write("\n")
                #ind+=1
'''
cos = []
for i in range(len(seq)):
    cos.append(numbering.count(i))
        
df = pd.DataFrame()
dic = dict(Counter(cos))
key = dic.keys()
value = dic.values()
sorted_keys = sorted(list(key))
sorted_values = []
for i in sorted_keys:
    sorted_values.append(dic[i])
print(Counter(cos))
df["No. of cases"] = sorted_keys
df["Count"] = sorted_values