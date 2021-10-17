# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:41:11 2021

@author: OK
"""

# 2021-10-13 crude oil


import os
from selenium import webdriver
import time
import logging
from selenium.webdriver.common.keys import Keys
import json



os.makedirs(r'C:\Users\OK\Desktop\프로젝트&공모전\2021\covid\data',exist_ok=True)

# 셀레니움 
options = webdriver.chrome.options.Options()
profile = {'download.default_directory':r'C:\Users\OK\Desktop\프로젝트&공모전\2021\covid\data'}
options.add_experimental_option('prefs',profile)
#leftColumn > div.mediumTitle1 > article:nth-child(2) > div.textDiv > a
driver = webdriver.Chrome(r'C:\Users\OK\Desktop\프로젝트&공모전\2021\크롤링\논문\chromedriver_win32\chromedriver.exe', options=options)


default_url = 'http://ncov.mohw.go.kr/'
driver.get(default_url)
X = []
X2 = []
for i in range(1,18):
    X.append(driver.find_element_by_css_selector('#main_maplayout1 > button:nth-child(%d)'%i).text)
    driver.find_element_by_css_selector('#main_maplayout1 > button:nth-child(%d)'%i).click()
    X2.append(driver.find_element_by_css_selector('#step_map_city%d'%i).text)    
driver.quit()

X = [i.split('\n') for i in X]
X2 = [i.split('\n') for i in X2]
X2

first = {i[0]:int(i[-1]) for i in X}
Second = {}
for i in X2:
    Second[i[0]] = {}
    Second[i[0]]['단계'] = i[1]
    Second[i[0]]['세부 단계 및 정보'] = '\n'.join(i[2:])

import time
import pickle
from datetime import datetime
d = datetime.today()
f = open(r'C:\Users\OK\Desktop\프로젝트&공모전\2021\covid\data\%d-%d-%d.json'%(d.year,d.month,d.day),'w')
j=json.dumps(Second)
json.dump(j,f)
