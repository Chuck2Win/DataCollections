# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:17:38 2021

@author: OK
"""
# Date : 2021-08-10
# 자막 파일 변환하기
import pysubs2 # srt, ass 자막에서 텍스트 뽑아내는 모듈
import re
import os
from tqdm import tqdm
import argparse
from utils import *
parser = argparse.ArgumentParser(description = '필요한 변수')

# Input data
parser.add_argument('--data_dir', default = r'C:\\Users\\OK\\Desktop\\프로젝트&공모전\\2021\\크롤링\\data', type = str)
parser.add_argument('--output_data_dir', default = r'C:\\Users\\OK\\Desktop\\프로젝트&공모전\\2021\\크롤링\\data\\text', type = str)

def Main():
    # 파일 확장자가 smi인 경우, 자막에서 텍스트 뽑아내기
    names = os.listdir(args.data_dir)
    for i in tqdm(names):
        #print(i)
        # encoding 방식 (utf-8, utf-16, ansi, euc-kr)
        #i = r'Big Love.2x11.Take Me as I Am.HDTV.XviD-Caph.Korean.smi'
        lines = read_any(i, args.data_dir)
        if lines!=[]:
            
            if i.endswith('srt'):
                new_path = args.output_data_dir+'/%s.txt'%i
                F = open(new_path,'w',encoding = 'utf-8')
                for l in lines:
                    sub_line = re.sub(r'\\N', ' ', l.text)
                    sub_line = re.sub(r"\<[^>]*\>"," ",sub_line).strip()
                    # {} 안의 것도 제
                    sub_line = re.sub(r"\{[^}]*\}"," ",sub_line).strip()
                    # 대괄호 안의 것들은 상황을 알려주는 경우가 많음,
                    sub_line = re.sub(r"\[[^]]*\]"," ",sub_line).strip()
                    # 괄호 역시 제거
                    sub_line = re.sub(r"\([^)]*\)"," ",sub_line).strip()
                    if sub_line:
                        F.write(sub_line+'\n')
            
            else:
            
        
                # 통합 자막 제외 하기 (즉 한국어만 get)
                # SYNC Start = value 에서 이 value가 감소하면 stop !!
                note_time = -float('inf')
                note_time_idx = -1
                start = -1
                end = -1
                count = 0
                
                for idx in range(len(lines)):
                    line = lines[idx].strip()
                        
                    
                    if line.lower().startswith(r'<sync start='):
                        #print(line)
                        # <sync start=><p class=krcc>&nbsp; 이런 경우가 존재.
                        # 음수인 경우도 있기에 [-0-9]
                        try:
                            num = re.findall('[-0-9]+',line)[0]
                            
                        except:
                            continue
                        temp = int(num)
                        #print(temp)
                        if start == -1:
                            start = idx
                            
                        if temp < note_time:
                            count += 1
                            if count == 5:
                                end = note_time_idx
                                break
                            
                        else:
                            note_time = temp
                            note_time_idx = idx
                            count = 0
                    else: 
                        continue
                else:
                    end = idx
                
                # 개 중에 SMI 형식이 아닌 경우가 있음.(SRT 형식인 경우)
                # 이 경우엔 제거함.
                if start == -1 or end == -1:
                    continue
                new_path = args.output_data_dir+'/%s.txt'%i
                F = open(new_path,'w',encoding = 'utf-8')
                x=[]
                lines
                for idx in range(start, end+1):
                    print(lines[idx])
                    line = lines[idx].strip()
                    #line
                    # 주로 sync 정보
                    sub_line = re.sub(r"\<[^>]*\>"," ",line).strip()
                    # {} 안의 것도 제
                    sub_line = re.sub(r"\{[^}]*\}"," ",sub_line).strip()
                    # 대괄호 안의 것들은 상황을 알려주는 경우가 많음,
                    sub_line = re.sub(r"\[[^]]*\]"," ",sub_line).strip()
                    # 괄호 역시 제거
                    sub_line = re.sub(r"\([^)]*\)"," ",sub_line).strip()
                    # &nbsp 제거하기 <- 줄바꿈을 나타내는 것임.
                    sub_line = re.sub("&nbsp"," ",sub_line).strip()
                    x.append(sub_line)
                
                    if sub_line:
                        #print(sub_line)
                        F.write(sub_line+'\n') # euc-kr로 하면 일본어 등이 카바가 안됨.
            F.close()
            
if __name__ == "__main__":
    args = parser.parse_args()
    Main()
