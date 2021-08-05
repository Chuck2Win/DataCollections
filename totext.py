# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:17:38 2021

@author: OK
"""
# Date : 2021-08-03
# 자막 파일 변환하기
import pysubs2 # srt, ass 자막에서 텍스트 뽑아내는 모듈
import re
import os
os.getcwd()
os.chdir('./data/곰')
names = os.listdir()
# 파일 확장자가 smi인 경우, 자막에서 텍스트 뽑아내기
Total_text_list = []
for i in names:
    
    if 'srt' not in i:
        # encoding 방식 (utf-8, utf-16, ansi, euc-kr)
        
        try:
            f = open(i,'r',encoding  = 'utf-8')
            lines = f.readlines()
        except:
            try:
                f = open(i,'r',encoding  = 'utf-16')
                lines = f.readlines()
            except:
                try:
                    f = open(i,'r',encoding  = 'ansi')
                    lines = f.readlines()
                except:
                    try:
                        f = open(i,'r',encoding  = 'cp949')
                        lines = f.readlines()
                    except:
                        try:
                            f = open(i,'r',encoding  = 'euc-kr')
                            lines = f.readlines()
                        except:
                            continue
            
        
        text = []
        processed_text = []
        for line in lines:
            line = line.strip()
            sub_line = re.sub(r"\<[^>]*\>","",line)
            if sub_line:
                processed_text.append(sub_line)
        Total_text_list.append(processed_text)
    else:
    # 파일 확장자가 srt인 경우 -> pysubs2 활용
    # encoding 방식 (utf-8, utf-16, ansi, euc-kr)
        
        try:
            lines = pysubs2.load(i,encoding  = 'utf-8')
        except:
            try:
                lines = pysubs2.load(i,encoding  = 'utf-16')
            except:
                try:
                    lines = pysubs2.load(i, encoding  = 'ansi')
                except:
                    try:
                        lines = pysubs2.load(i, encoding = 'cp949')
                    except:
                        try:
                            lines = pysubs2.load(i, encoding  = 'euc-kr')
                        except:
                            continue
        text_list = []
        for l in lines:
            text_list.append(l.text)
            Total_text_list.append(processed_text)
            

