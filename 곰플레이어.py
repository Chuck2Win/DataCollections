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
from bs4 import BeautifulSoup
import time
import selenium.webdriver.support.ui as ui

# 셀레니움 
# ChromeDrive가 있는 절대 경로.
chromedriver = 'C:/Users/OK/Desktop/프로젝트&공모전/2021/크롤링/chromedriver.exe'

# 다운로드 경로 변경
options = webdriver.chrome.options.Options()
profile = {'download.default_directory':r'C:\Users\OK\Desktop\프로젝트&공모전\2021\크롤링\data'}
options.add_experimental_option('prefs',profile)
# Chrome으로 활용
driver = webdriver.Chrome(chromedriver,options=options)
# 1초 정도 기다리게 해줌
driver.implicitly_wait(1)

# 해당 드라이버로 이동(한국어만,preface=kr)
default_url = 'https://www.gomlab.com/subtitle/?preface=kr&page='
driver.get(default_url)

Test= []
cnt = 0
while True:
    print('Page'+str(cnt))
    if cnt>0: # 원하는 페이지의 수
        break
    cnt+=1
    driver.get(default_url+str(cnt)) # go here !
    driver.implicitly_wait(1)
    posts = driver.find_elements_by_class_name('subject > a')
    links = [post.get_attribute('href') for post in posts]
    for link in links:
        driver.get(link)
        if driver.find_elements_by_xpath("//a[@class='btn']"):
            # click button 누르기
            first_link = driver.find_elements_by_xpath("//a[@class='btn']")[0].click()
            #first_link = ui.WebDriverWait(driver, 30).until(lambda browser: browser.find_element_by_xpath("/a[@title='다운로드']")).click()
        #https://www.gomlab.com/subtitle/download.gom?seq=221855
        # <a class = 'btn_type3 download'>로 이뤄진 값의 위치를 찾아냄. 
#driver.find_elements_by_xpath("//a[@class='btn']")[0].click()
################################################
# 언어 선택
# 다운로드.. ㅁ        
#print(links)
#link
driver.quit()
