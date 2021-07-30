# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:17:38 2021

@author: OK
"""

# every time 크롤링
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import os

# 셀레니움 <- 거의 매크로 같은 기능을 해줌.
# 절대 경로로 해줘야함.
chromedriver = 'C:/Users/OK/Desktop/프로젝트&공모전/2021/크롤링/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
# 1초 정도 기다리게 해줌
driver.implicitly_wait(1)

# crawling for any pages
driver.get('http://everytime.kr/login')
# id, password
driver.find_element_by_name("userid").send_keys("user id")
driver.find_element_by_name("password").send_keys("password")
# 로그인을 해줌.
driver.find_element_by_tag_name("input").send_keys(Keys.RETURN)
driver.implicitly_wait(1)


# driver.quit()

# # 자게만 해야겠. 370440

###########################################
results = []
Test= []
cnt = 0
while True:
    print('Page'+str(cnt))
    if cnt>3: # 원하는 페이지의 수
        break
    cnt+=1
    # https://everytime.kr/ -> 뒤에 370440 은 자유 게시판을 의미하는 것임.
    driver.get("https://everytime.kr/370440/p/"+str(cnt)) # go here !
    driver.implicitly_wait(1)
    
    # get article link
    #driver
    # css 형태로 검색했고, article 밑에 a.article이 있는 경우를 찾아옴.
    # post 아래에 article 그 밑에 article로 가서 링크를 가져온다.
    posts = driver.find_elements_by_css_selector('article > a.article') # >는 하위를 의미함
    # 그 다음에 href -> 주소를 가져옴.
    posts[0].get_attribute('href')
    links = [post.get_attribute('href') for post in posts]
    
    for link in links:
        driver.get(link)
        comments = driver.find_elements_by_css_selector('p.large')
        for comment in comments:
            results.append(comment.text)
        