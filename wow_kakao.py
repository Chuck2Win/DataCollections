# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 17:12:47 2021

@author: OK
"""
import os
import sys
from kakaotrans import Translator

translator = Translator()

def translate(sentences):
    return translator.translate(sentences, src = 'en', tgt = 'kr')

# 번역기 돌리기
import json
import copy
f=open(r'G:\데이터\WoW\wizard_of_wikipedia\train.json','rb')
data = json.load(f)
kor_data = copy.deepcopy(data)

import logging
logger = logging.getLogger('logger') # 적지 않으면 root로 생성
# 2. logging level 지정 - 기본 level Warning
logger.setLevel(logging.INFO)
# 3. logging formatting 설정 - 문자열 format과 유사 - 시간, logging 이름, level - messages
formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s] >> %(message)s')
file_handler = logging.FileHandler('log.txt', encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

##################################
from tqdm import tqdm

for i in tqdm(range(1,len(data))): # dict_keys(['speaker', 'text', 'checked_sentence', 'checked_passage', 'retrieved_passages', 'retrieved_topics'])
#i = 0
    logger.info('%d번째 data'%(i+1))
    kor_data[i]['chosen_topic'] = translate(data[i]['chosen_topic']) # 번역
    #s = 0
    for j in range(len(data[i]['dialog'])):
        #s+=len(data[i]['dialog'][j]['text'])
        kor_data[i]['dialog'][j]['text']=translate(data[i]['dialog'][j]['text'])
        
        #kor_data[i]['dialog'][j]['retrieved_passages'] # 번역해야함.
        for k in range(7):
            a=kor_data[i]['dialog'][j]['retrieved_passages'][k] # 번역해야함.
            #x = [len(i) for i in list(kor_data[i]['dialog'][j]['retrieved_passages'][k].values())[0]]
            x=[translate(i) for i in list(kor_data[i]['dialog'][j]['retrieved_passages'][k].values())[0]]
            #s+=sum(x)
            kor_data[i]['dialog'][j]['retrieved_passages'][k][translate(list(a.keys())[0])]=x
   


import pickle
f=open(r'G:\데이터\WoW\wizard_of_wikipedia\train_kor','wb')
pickle.dump(kor_data,f)
