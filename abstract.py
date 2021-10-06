
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 15:26:59 2021
@author: OK
"""
# 논문 다운로드 
# 한국 학술지 인용 색인
# 'https://www.kci.go.kr/kciportal/po/search/poArtiSearList.kci'
# 1843210 개
import os
from selenium import webdriver
from urllib.request import urlopen
import time
import pickle
from tqdm import tqdm
import logging

if __name__ == '__main__':

    logger1 = logging.getLogger('abstract_log')
    logger1.setLevel(logging.INFO)
    
    logger2 = logging.getLogger('abstract_log_stream')
    logger2.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s- %(message)s')
    file_handler = logging.FileHandler(r'C:\Users\OK\Desktop\프로젝트&공모전\2021\크롤링\논문\download_abstract_page.txt',encoding='utf-8')
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger1.addHandler(file_handler)
    logger2.addHandler(stream_handler)
    
    os.makedirs(r'C:\Users\OK\Desktop\프로젝트&공모전\2021\크롤링\논문',exist_ok=True)
    # 셀레니움 
    
    options = webdriver.chrome.options.Options()
    #options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')
    save_dir = r'C:\Users\OK\Desktop\프로젝트&공모전\2021\크롤링\논문\data'
    
    default_url = 'https://www.kci.go.kr/kciportal/po/search/poArtiSearList.kci'
    
    driver = webdriver.Chrome(r'C:\Users\OK\Desktop\프로젝트&공모전\2021\크롤링\논문\chromedriver_win32\chromedriver.exe', options=options)
    next_button = '#contents > div > div.search-answer-list > div > a:nth-child(13)'
    driver.get(default_url)
    before = None
    cnt = 1
    content_cnt = 1
    now = time.time()
    while True:
        logger2.info('%d page'%cnt)
        # url list 
        current = driver.find_element_by_css_selector('#contents > div > div.search-answer-list > div > span').text
        if before is None:
            before = current
        else:
            if before == current:
                logger1.info('download end')
                break
            
        first = driver.find_elements_by_css_selector('#poArtiSearList > table > tbody > tr')
        # url
        urls = [i.find_element_by_css_selector('td:nth-child(3)>a').get_attribute('href') for i in first]
        # title
        titles = [i.find_element_by_class_name('subject').text for i in first]
        for j,i in zip(titles,urls):
            driver.get(i)
            candi = driver.find_element_by_css_selector('#reportDetail > div.report-detail-left > div > div:nth-child(1) > div')
            try:
                tmp1=candi.find_element_by_id('korAbst').text
                tmp2=candi.find_element_by_id('engAbst').text
                if tmp1==tmp2:
                    driver.back()
                    continue
                f = open(os.path.join(save_dir,j+'.txt'),'w',encoding='utf-8')
                f.write(tmp1)
                f.write('\n')
                f.write(tmp2)
                driver.back()
                logger1.info('%d file'%content_cnt)
                content_cnt+=1
            except:
                driver.back()
                continue
            
        next_button = '#contents > div > div.search-answer-list > div > a:nth-child(13)'
        target = driver.find_element_by_css_selector(next_button)
        driver.execute_script("arguments[0].scrollIntoView(true);", target) # target이 있을 때까지 스크롤 다운
        time.sleep(1)
        driver.find_element_by_css_selector(next_button).click()
        before = current
        cnt+=1
    print(time.time()-now)
