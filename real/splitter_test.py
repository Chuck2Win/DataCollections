# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:19:42 2021

@author: OK
"""
data = """진리?
진리는 무엇인가?
여기 많은 사람들이 네가 악령을 부려서 병을 고치고
하나님의 역사라 부르는 것을 보았다!
많은 이들이
네가 성전을 파괴하고
3일 만에 또 다른 성전을
세울 것이라는 너의 말을 들었다.
여기 산헤드린  앞에서 누군가는
네가 이 말을 했다는 것을 증언할 것이다.
너의 답변은 어떠한가?
답변을 거부할 것인가?
네가 메시아인가
아닌가?
내가 그렇소.
그리고 머지않아 당신은 인자가
하나님의 우편에 앉는 것을 볼 것이오.
어찌 감 네가
그 분의 이름을 말하는가?!
죄목은 신성모독이다.
사형에 해당한다!
유다!
당신.
당신도 한패지!
아니.
난 아니오.
"""

# -*- coding: utf-8 -*-

import re
import os
import kss
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(description = '필요한 변수')
# Input data
parser.add_argument('--data_dir', default = r'C:\\Users\\OK\\Desktop\\프로젝트&공모전\\2021\\크롤링\\data\\text\\preprocessed_data', type = str)
parser.add_argument('--output_data_dir', default = r'C:\\Users\\OK\\Desktop\\프로젝트&공모전\\2021\\크롤링\\data\\text\\preprocessed_data_2', type = str)
args = parser.parse_args()

data    
new_doc = [sent for sent in kss.split_sentences(' '.join(data.split('\n')))]
new_doc        
kss.split_sentences(data,backend=
data2 = data
data2
data2 = re.sub('[?!.]','', data2)
data2

new_doc2 = [sent for sent in kss.split_sentences(' '.join(data2.split('\n')))]
new_doc2
data2
data
print(data)
print('\n'.join(new_doc))
print('\n'.join(new_doc2))
