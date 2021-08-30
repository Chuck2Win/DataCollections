import os
path = r'C:\Users\OK\Desktop\프로젝트&공모전\2021\크롤링\data\text\preprocessed_data\\MV'
names=os.listdir(r'C:\Users\OK\Desktop\프로젝트&공모전\2021\크롤링\data\text\preprocessed_data\\MV')
D = {}
for i in names:
    
    f = open(os.path.join(path,i),'r',encoding='utf-8')
    x=f.read().split('\n')
    D[i]=x
    
L = list(map(len,list(D.values())))

max(L)

import numpy as np

np.percentile(L,[95,97,99])

for i,j in D.items():
    if len(j)==283:
        print(i)