# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:05:21 2021

@author: OK
"""
import pysubs2 

def read_any(i,data_dir):
    encodings = ['utf-8','utf-16','ansi','cp949','euc-kr']
    lines = []
    for e in encodings:
        try:
            if 'srt' in i:
                lines = pysubs2.load(i,encoding = e)
            
            else:
                f = open(data_dir+'/'+i,'r',encoding  = e)
                lines = f.readlines()
                f.close()
            break
        except:
            continue
    return lines