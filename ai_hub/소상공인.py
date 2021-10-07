import pandas as pd
import os
from tqdm import tqdm

output_dir = r'/data/nlp/ai_data/ok_0915/NIA_1007'
data_dir = r'/data/nlp/ai_data/NIA/소상공인 고객 주문 질의-응답 텍스트/Training'
data_dir2 = r'/data/nlp/ai_data/NIA/소상공인 고객 주문 질의-응답 텍스트/Validation'



data_list = [i for i in os.listdir(data_dir) if i.endswith('csv')]
F = open(os.path.join(output_dir,'소상공인.txt'),'w',encoding='utf-8')
for i in data_list:
    print(i)
    try:
        data = pd.read_csv(os.path.join(data_dir,i),header=0,error_bad_lines=False)
    except:
        continue
    current = None
    for j in tqdm(data.index):
        if current is None:
            current = data['QA번호'][j]
        if current!=data['QA번호'][j]:
            F.write('\n')
            F.write(data['발화문'][j])
            F.write('\n')
            current = data['QA번호'][j]
        else:
            F.write(data['발화문'][j])
            F.write('\n')

data_list = [i for i in os.listdir(data_dir2) if i.endswith('csv')]

for i in data_list:
    print(i)
    try:
        data = pd.read_csv(os.path.join(data_dir2,i),header=0,error_bad_lines=False)
    except:
        continue
    current = None
    for j in tqdm(data.index):
        if current is None:
            current = data['QA번호'][j]
        if current!=data['QA번호'][j]:
            F.write('\n')
            F.write(data['발화문'][j])
            F.write('\n')
            current = data['QA번호'][j]
        else:
            F.write(data['발화문'][j])
            F.write('\n')
            
F.close()
