import json 
import os
from tqdm import tqdm
data_dir = '/data/nlp/ai_data/NIA/민원(콜센터)_질의-응답_데이터/Training/data'
output_dir = '/data/nlp/ai_data/ok_0915/NIA_1007'

data_list = os.listdir(data_dir)
F = open(os.path.join(output_dir,'민원.txt'),'w',encoding='utf-8')
for i in data_list:
    f = open(os.path.join(data_dir,i),'r',encoding='cp949')
    data = json.load(f)
    current = None
    current_usr = None
    current_utter= ''
    for j in tqdm(data):
        if current is None:
            current=j['대화셋일련번호']
            current_usr = j['화자']
        if current==j['대화셋일련번호']:
            if current_usr == j['화자']:
                utter = j['고객질문(요청)']+j['상담사질문(요청)']+j['고객답변']+j['상담사답변']
                current_utter=current_utter+' '+utter
            else:
                F.write(current_utter)
                F.write('\n')
                current_user = j['화자']
                current_utter = j['고객질문(요청)']+j['상담사질문(요청)']+j['고객답변']+j['상담사답변']
        else:
            # 다른 대화 셋이라면
            F.write(current_utter)
            F.write('\n\n')
            current = j['대화셋일련번호']
            current_usr = j['화자']
            current_utter = j['고객질문(요청)']+j['상담사질문(요청)']+j['고객답변']+j['상담사답변']
    F.write(current_utter)
    F.write('\n\n')
F.close()        
        
        

