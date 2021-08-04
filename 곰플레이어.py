# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:17:38 2021

@author: OK
"""
# Date : 2021-08-02
# 곰플레이어 자막 크롤링

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import time
import selenium.webdriver.support.ui as ui
now = time.time()
# 셀레니움 
# ChromeDrive가 있는 절대 경로.
chromedriver = 'C:/Users/OK/Desktop/프로젝트&공모전/2021/크롤링/chromedriver.exe'

# 다운로드 경로 변경
options = webdriver.chrome.options.Options()
profile = {'download.default_directory':r'C:\Users\OK\Desktop\프로젝트&공모전\2021\크롤링\data\곰'}
options.add_experimental_option('prefs',profile)
# Chrome으로 활용
options.add_argument("headless")
driver = webdriver.Chrome(chromedriver,options=options)
# 1초 정도 기다리게 해줌
# 해당 드라이버로 이동(한국어만,preface=kr)
default_url = 'https://www.gomlab.com/subtitle/?preface=kr&page='
driver.get(default_url)
# url list 
download_url = []
cnt = 0
while True:
    
    if cnt>4:
        break
    print('Page'+str(cnt))
    cnt+=1
    try:
        driver.get(default_url+str(cnt)) # go here !
    except:
        break
    #driver.implicitly_wait(1)
    posts = driver.find_elements_by_class_name('subject > a')
    links = [post.get_attribute('href') for post in posts]
    download_url.extend(links)
    
for link in download_url:
    driver.get(link)
    if driver.find_elements_by_xpath("//a[@class='btn']"):
        # click button 누르기
        first_link = driver.find_elements_by_xpath("//a[@class='btn']")[0].click()
driver.quit()
after = time.time()
print(after-now)

