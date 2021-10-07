import os
import json
from tqdm import tqdm
input_dir = r'/data/nlp/ai_data/NIA/한국어_SNS/Training'
output_dir =r'/data/nlp/ai_data/ok_0915/NIA_1007'
#    cmd +/data/nlp/ai_data/ok_0915/= f"--split_by_whitespace=false "
data_list = os.listdir(input_dir)
F = open(os.path.join(output_dir, '한국어_SNS.txt'),'w',encoding='utf-8')    
for i in data_list:
    print(i)
    f=open(os.path.join(input_dir, i))
    data = json.load(f,strict=False)
    for j in tqdm(data['data']):
        
        current_user = None
        current_utter = None
        for k in j['body']:
            if current_user is None:
                current_user = k['participantID']
                current_utter= k['utterance']
            else:
                if current_user != k['participantID']:
                    F.write(current_utter)
                    F.write('\n')
                    current_utter = k['utterance']
                    current_user = k['participantID']
                else:
                    current_utter=current_utter+' '+k['utterance']
        F.write(current_utter)
        F.write('\n\n')
F.close()
            

