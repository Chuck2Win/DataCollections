# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 15:26:59 2021

@author: OK
"""
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import time
import selenium.webdriver.support.ui as ui
import pickle
from tqdm import tqdm
import logging

if __name__ == '__main__':

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s- %(message)s')
    file_handler = logging.FileHandler('download_gom_1.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # 셀레니움 
    # 다운로드 경로 변경
    options = webdriver.chrome.options.Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    profile = {'download.default_directory':r'C:\Users\OK\Desktop\프로젝트&공모전\2021\크롤링\data',}
    options.add_experimental_option('prefs',profile)
    driver = webdriver.Chrome(r'C:/Users/OK/Desktop/프로젝트&공모전/2021/크롤링/chromedriver.exe', options=options)
    
    # 해당 드라이버로 이동(한국어만,preface=kr)
    default_url = 'https://www.gomlab.com/subtitle/?preface=kr&page='
    driver.get(default_url)
    
    # url list 
    download_url = []
    cnt = 12000
    end = 18241
    
    for cnt in tqdm(range(cnt+1,end+1),mininterval=60):
        try:
            # 여기에 가도 우리가 원하는 데이터가 없을 수 있음
            driver.get(default_url+str(cnt)) # go here !
            posts = driver.find_elements_by_class_name('subject > a')
            if posts!=[]:
                links = [post.get_attribute('href') for post in posts]
                for link in links:
                    logger.info(f'{link}')
                    driver.get(link)
                    if driver.find_elements_by_xpath("//a[@class='btn']"):
                        # click button 누르기
                        first_link = driver.find_elements_by_xpath("//a[@class='btn']")[0].click()
                    
                # print(download_url)
            else:
                break
        except:
            break
    driver.quit()
