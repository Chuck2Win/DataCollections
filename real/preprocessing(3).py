# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:51:44 2021

@author: OK
"""
import re
import os
import kss
from tqdm import tqdm
import argparse
import time

# KSS SPLIT

parser = argparse.ArgumentParser(description = '필요한 변수')
# Input data
parser.add_argument('--data_dir', default = r'C:\\Users\\OK\\Desktop\\프로젝트&공모전\\2021\\크롤링\\data\\text\\preprocessed_data', type = str)
parser.add_argument('--output_data_dir', default = r'C:\\Users\\OK\\Desktop\\프로젝트&공모전\\2021\\크롤링\\data\\text\\preprocessed_data_2', type = str)
#kss.split_chunks()
if __name__ == "__main__":
    
    args = parser.parse_args()
    name = os.listdir(args.data_dir)
    N = []
    for i in tqdm(name):
        f = open(os.path.join(args.data_dir,i),'r',encoding='utf-8')
        x = f.read()
        doc = re.sub('\n', ' ', x)
        now = time.time()
        new_doc = kss.split_sentences(doc)
        N.append(new_doc)
        #print(time.time()-now)
        f = open(os.path.join(args.output_data_dir,i),'w')
        for j in new_doc:
            f.write(j+'\n')
        f.close()

