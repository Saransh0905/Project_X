#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:37:37 2019

@author: saransh
"""

import scrapy,csv
from scrapy.http import Request
import pandas as pd


l = []
#with open ("/home/saransh/Documents/Github/Project_X/Blasted.csv","r") as data:
data = pd.read_csv("/home/saransh/Documents/Github/Project_X/Blasted.csv")
col = data["subject acc.ver"].values
ur = "https://www.ncbi.nlm.nih.gov/search/all/?term="
for i in col:
    to_append = ur+str(i)
    print(to_append)
    l.append(to_append)

    #scrapy.Spider.start_urls = [l[1]]
class Protease(scrapy.Spider):
    global l
    #start_urls = l
    start_urls = [l[0]]
    name = 'Protease'
    def __init__(self):
        self.infile = open("final_output.csv","w",newline="")

    def start_requests(self):
        for link in self.start_urls:
            print(self.start_urls)
            print('hellohellohel-----------hello',str(link))
            
            yield self.make_requests_from_url(url = str(link))
        print('_______________',str(l[0]))
    def parse(self,response):
        #response = response[1]
        #print(response.url)
        GO_MF = response.xpath('//*[(@id = "sequence_title")]//a/text()').extract()
        K_MF = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "ncbi-doc-authors", " " ))]//a/text()').extract()
        combined = GO_MF + K_MF
        writer = csv.writer(self.infile)
        writer.writerow(combined)

        yield {
            'entry': combined
        } 
        #print("_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_-_-_-__-_-_-_--___-___-___-__-___-____-_-_-_-_-_-_-_-____-__-_-_-_")   
        