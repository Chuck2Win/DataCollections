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
import time
import logging

if __name__ == '__main__':

    logger1 = logging.getLogger('abstract_log2')
    logger1.setLevel(logging.INFO)
    
    logger2 = logging.getLogger('abstract_log_stream2')
    logger2.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s- %(message)s')
    file_handler = logging.FileHandler(r'C:\Users\dialog\Desktop\논문\download_abstract_page.txt',encoding='utf-8')
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger1.addHandler(file_handler)
    logger2.addHandler(stream_handler)
    
    os.makedirs(r'C:\Users\dialog\Desktop\논문\data',exist_ok=True)
    # 셀레니움 
    
    options = webdriver.chrome.options.Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    save_dir = r'C:\Users\dialog\Desktop\논문\data'
    
    default_url = 'https://www.kci.go.kr/kciportal/po/search/poArtiSearList.kci'
    
    driver = webdriver.Chrome(r'C:\Users\dialog\Desktop\논문\chromedriver_win32\chromedriver.exe', options=options)
    next_button = '#contents > div > div.search-answer-list > div > a:nth-child(13)'
    driver.get(default_url)
    before = '0'
    current = driver.find_element_by_css_selector('#contents > div > div.search-answer-list > div > span').text
    cnt = 1
    content_cnt = 1
    while True:
        logger2.info(current+' page')
        # url list 
        current = driver.find_element_by_css_selector('#contents > div > div.search-answer-list > div > span').text
        if before == current:
            logger1.info('download end')
            break
            
        first = driver.find_elements_by_css_selector('#poArtiSearList > table > tbody > tr')
        # url
        urls = [i.find_element_by_css_selector('td:nth-child(3)>a').get_attribute('href') for i in first]
        # title
        titles = [i.find_element_by_class_name('subject').text for i in first]
        for _,(j,i) in enumerate(zip(titles,urls)):
            logger1.info(j)
            driver.get(i)
            candi = driver.find_element_by_css_selector('#reportDetail > div.report-detail-left > div > div:nth-child(1) > div')
            try:
                tmp1=candi.find_element_by_id('korAbst').text
                tmp2=candi.find_element_by_id('engAbst').text
                if tmp1==tmp2:
                    # 보통 영어임 -> 영어만 저장
                    tmp1=candi.find_element_by_id('korAbst').text
                    f = open(os.path.join(save_dir,'eng','%d.txt'%_),'w',encoding='utf-8')
                    f.write(j)
                    f.write('\n\n')
                    f.write(tmp1)
                    f.write('\n\n')
                    f.close()
                    driver.back()
                    

                f = open(os.path.join(save_dir,'eng_kor','%d.txt'%_),'w',encoding='utf-8')
                f.write(j)
                f.write('\n\n')
                f.write(tmp1)
                f.write('\n\n')
                f.write(tmp2)
                f.close()
                driver.back()
                
                
            except:
                # just english
                try:
                    tmp1=candi.find_element_by_id('korAbst').text
                    
                    f = open(os.path.join(save_dir,'eng','%d.txt'%_),'w',encoding='utf-8')
                    f.write(j)
                    f.write('\n\n')
                    f.write(tmp1)
                    f.close()
                    driver.back()
                    
                except:
                    try:
                        tmp2=candi.find_element_by_id('engAbst').text
                        f = open(os.path.join(save_dir,'eng','%d.txt'%_),'w',encoding='utf-8')
                        f.write(j)
                        f.write('\n\n')
                        f.write(tmp2)
                        f.close()
                        driver.back()
                    except:
                        driver.back()
                        continue
                    
            
        next_button = '#contents > div > div.search-answer-list > div > a:nth-child(13)'
        target = driver.find_element_by_css_selector(next_button)
        driver.execute_script("arguments[0].scrollIntoView(true);", target) # target이 있을 때까지 스크롤 다운
        time.sleep(1)
        #driver.implicitly_wait(1)
        driver.find_element_by_css_selector(next_button).click()
        driver.implicitly_wait(1)
        before = current
        cnt+=1
    
