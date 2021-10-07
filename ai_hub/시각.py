import json
import pandas as pd 
import os
from tqdm import tqdm
data_dir = '/data/nlp/ai_data/NIA/시각정보기반'
output_dir = '/data/nlp/ai_data/ok_0915/NIA_1007'



for a in ['Training','Validation']:
    cur_data_dir = os.path.join(data_dir,a)
    
    data_list = os.listdir(cur_data_dir)
    for i in data_list:
        inner_cur_data_dir = os.path.join(cur_data_dir,i)
        inner_data_list = os.listdir(inner_cur_data_dir)    
        for j in inner_data_list:
            inner_inner_path = os.path.join(inner_cur_data_dir,j)
            
            inner_inner_data_list = os.listdir(inner_inner_path)
#            F = pd.DataFrame()
            anno = json.load(open(os.path.join(inner_inner_path, 'annotation.json'),'rb'))
            anno = anno['annotations']
            ques = json.load(open(os.path.join(inner_inner_path,'question.json'),'rb'))
            ques = ques['questions']
            an = pd.DataFrame()
            qe = pd.DataFrame()
            a = []
            idx = []
            q = []
            for e in range(len(anno)):
                a.append(anno[e]['multiple_choice_answer'])
                idx.append(anno[e]['question_id'])
            an['idx']=idx
            an['answer']=a
            q2 = []
            for e in range(len(ques)):
                q.append(ques[e]['question'])
                q2.append(ques[e]['question_id'])
            qe['idx']=q2
            qe['question']=q
            final_space = pd.merge(qe,an,how='inner',on='idx')
            final_space.to_csv(os.path.join(output_dir,j))
                        
                    


        
        

