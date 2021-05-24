#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_1=pd.DataFrame(np.random.rand(500,3),
        columns=['A','B','C'])
print(data_1.describe())
data_1['AA']=pd.Series(list(range(len(data_1))))
data_1.plot(x='AA')
plt.show()

data_2=pd.DataFrame(np.random.rand(10,4))
data_2.plot(kind='bar')
plt.show()

pairs=[]
data_3=pd.read_excel('./data/电影导演演员.xlsx')
for i in range(len(data_3)):
    actors=data_3.at[i,'演员'].split(',')
    print(actors)
    for actor in actors:
        pair=(actor,data_3.at[i,'电影名称'])
        pairs.append(pair)

pairs=sorted(pairs,key=lambda item:int(item[0][2:]))
print(pairs)
index=[item[0] for item in pairs]
data=[item[1] for item in pairs]
