#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 21:20:17 2019

@author: saransh
"""

from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond



data = pd.read_csv("/home/saransh/Documents/Github/Project_X/Blasted.csv")
df = pd.DataFrame()
l_name = []
l_typo = []
main = []
col = data["subject acc.ver"].values
ur = "https://www.ncbi.nlm.nih.gov/search/all/?term="
driver = webdriver.Chrome(executable_path="/home/saransh/Downloads/chromedriver_linux64/chromedriver")

for i in range(87,262):
    driver.implicitly_wait(3)
    url = ur+col[i]
    main.append(col[i])
# Now create an 'instance' of your driver
# This path should be to wherever you downloaded the driver

# A new Chrome (or other browser) window should open up
    driver.get(url)
    id_name  = driver.find_element_by_id("sequence_title")
    id_type = driver.find_element_by_class_name("ncbi-doc-authors")
    name = id_name.get_attribute("innerHTML")
    name  = name[21:len(name)]
    typo = id_type.get_attribute("innerHTML")
    
    l_name.append(str(name))
    l_typo.append(typo)
    print(typo)
    driver.close()
    driver = webdriver.Chrome(executable_path="/home/saransh/Downloads/chromedriver_linux64/chromedriver")
df["Main"] = main
df["NAME"] = l_name
df["type"] = l_typo
#print(df)
df.to_csv("/home/saransh/Documents/Github/Project_X/final_out2.csv")
    
    #wait.until(cond.number_of_windows_to_be(3))
#('//*[(@id = "sequence_title")]'))