# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:17:38 2021

@author: OK
"""
# Date : 2021-08-10
# 자막 전처리 작업
import re
import os
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(description = '필요한 변수')
# Input data
parser.add_argument('--data_dir', default =r'C:\\Users\\OK\\Desktop\\프로젝트&공모전\\2021\\크롤링\\data\\text', type = str)
parser.add_argument('--output_data_dir', default = r'C:\\Users\\OK\\Desktop\\프로젝트&공모전\\2021\\크롤링\\data\\text\\preprocessed_data', type = str)

parser.add_argument('--stopword', default = r'C:\\Users\\OK\\Desktop\\프로젝트&공모전\\2021\\크롤링\\data\\text\\stopword\\stopword.txt', type = str)
parser.add_argument('--check_length', default = 64, type = int)


# 1. 영어, 숫자, 한글, 빈칸, 구두점, 쉼표, 물음표, 느낌표, 콜론 외엔 제거
# 2. 전 후로 check length만큼 stop word가 있을 경우 해당 row 제거
# 3. threshold 이상 이 영어 인 경우 해당 자막 데이터 제거
# 4. 한국어 영어가 섞인 경우 제거

def leave(doc):
    new_doc = []
    for sentence in doc:
        x = re.sub('[^a-zA-Z0-9 ,.:?!ㄱ-ㅎㅏ-ㅣ가-힇]*','',sentence).strip()
        if x:
            new_doc.append(x)
    return new_doc


# 시작, 끝에서 check length (줄 수) 만큼 stop word가 있는 지를 파악



def check_trash(doc, check_length, stopword):
    if len(doc)>=2*check_length:
        new_doc = doc[check_length:-check_length]
        start = []
        end = []
        for idx in range(check_length):
            for i in stopword:
                if doc[idx].lower().find(i.lower())!=-1:
                    break
                else:
                    continue
            else:
                start.append(doc[idx])
        for idx in range(-check_length,-1,1):
            for i in stopword:
                if doc[idx].lower().find(i.lower())!=-1:
                    break
                else:
                    continue
            else:
                end.append(doc[idx])
        new_doc = start + new_doc + end    
    else:
        new_doc = []
        for idx in range(len(doc)):
            for i in stopword:
                if doc[idx].lower().find(i.lower())!=-1:
                    break
                else:
                    continue
            else:
                new_doc.append(doc[idx])
        
    return new_doc

# 앞 뒤로 같은 문장일 경우 squeeze
def squeeze(doc):
    new_doc= []
    for idx in range(len(doc)-1):
        before = re.sub(' ','',doc[idx])
        after = re.sub(' ','',doc[idx+1])
        if before!=after:
            new_doc.append(doc[idx])
    try:
        if re.sub(' ','',doc[-2])!=re.sub(' ','',doc[-1]):
            new_doc.append(doc[-1])
    except:
        # 길이가 짧다는 것임.
        new_doc.append(doc[-1])
        # print(doc[-2])
        # print(doc[-1])
    return new_doc    

def is_eng(doc):
    kr_c = 0
    en_c = 0
    for sentence in doc:
        en_c += len([i for i in re.findall('[a-zA-Z]*', sentence) if i])
        kr_c += len([i for i in re.findall('[ㄱ-ㅎㅏ-ㅣ가-힇]*', sentence) if i ])
    if en_c/(kr_c+en_c+1e-8) >= 0.9:
        return True
    else:
        return False
        
# 한국어 영어
def split_kor_eng(doc):
    cnt = 0
    check_idx = -1
    for idx in range(len(doc)):
        kr_c = len([i for i in re.findall('[ㄱ-ㅎㅏ-ㅣ가-힇]*', doc[idx]) if i ])
        if kr_c == 0:
            cnt+=1
            if cnt>=10:
                break
            
        else:
            check_idx = idx
            cnt = 0
    return doc[:(check_idx+1)]

def main(stopword):
    # 파일 확장자가 smi인 경우, 자막에서 텍스트 뽑아내기
    names = os.listdir(args.data_dir)#[:1]
    
    for i in tqdm(names):
        try:
             f = open(os.path.join(args.data_dir,i),'r',encoding  = 'utf-8')
             lines = f.read().split('\n')
             f.close()
        except:
            continue
    # 1. a
        doc = leave(lines)
        #2. 
        doc = check_trash(doc,args.check_length, stopword)
        #3. 
        
        if doc != []:
            # new_path = os.path.join(args.output_data_dir,'before_eng')
            # F = open(os.path.join(new_path,i),'w',encoding='utf-8')
            # F.write('\n'.join(doc))
            # F.close()
            if not is_eng(doc):
                if doc!=[]:
                    doc = split_kor_eng(doc)
                    if doc!=[]:
                        doc = squeeze(doc)
                        if doc!=[]:
                            F = open(os.path.join(args.output_data_dir,i),'w',encoding='utf-8')
                            F.write('\n'.join(doc))
                            F.close()

if __name__ == "__main__":
    args = parser.parse_args()
    test_path_before = os.path.join(args.output_data_dir,'before_eng')
    os.makedirs(test_path_before,exist_ok=True)
    os.makedirs(args.output_data_dir,exist_ok=True)
    
    f = open(args.stopword,'r',encoding = 'utf-8')
    stopword = f.read().split('\n')
    main(stopword)