#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 19:32:06 2019

@author: saransh
"""

fasta = open('/home/saransh/Documents/Project_X/Project_X/RAW_data/T.solium_proteases_280.txt','r')
count = 0
till30 = 1
i = 1
new = open("toblast"+str(i),"a")

for line in fasta:
    
    if line[0]==">":
        count+=1
        till30+=1
        if till30==30 or count==262:
            new.close()
            i+=1
            new = open("toblast"+str(i),"a")
            till30=1
    new.write(line)

new.close()            
            