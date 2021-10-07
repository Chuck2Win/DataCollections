import json
import pandas as pd 
import os
from tqdm import tqdm
data_dir = '/data/nlp/ai_data/ok_0915/NIA_1007/시각/NIA_1007'
output_dir = '/data/nlp/ai_data/ok_0915/NIA_1007'
data_list = os.listdir(data_dir)
F = open(os.path.join(output_dir,'시각.txt'),'w',encoding='utf-8')
check_length_1 = 0
check_length_2 = 0
c = 0
for i in data_list:
    data = pd.read_csv(os.path.join(data_dir,i),index_col=0,header=0)
    data = data.dropna()
    for j in data.index:
        
        F.write(data['question'][j])
        check_length_1+=len(data['question'][j])
        F.write('\n')
        F.write(data['answer'][j])
        check_length_2+=len(data['answer'][j])
        F.write('\n\n')                    
        c+=1
F.close()
print(check_length_1/c)
print(check_length_2/c)
                    


        
        

