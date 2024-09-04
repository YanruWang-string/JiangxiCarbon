import  pandas as pd
import numpy as np
import json
import copy
dict={}
dict2={}
all=[]
Data=pd.read_excel("./data/山东省各市2000-2019年绿化率.xlsx")
indicator=Data.columns[1:].tolist()#获取到1997-2019时间点
for i in indicator:
    arr=Data[i].tolist()
    # print(arr)
    for j in range(len(arr)):
        dict['name']=Data['city'][j]
        dict['value']=arr[j]
        # print(dict)
        all.append(copy.deepcopy(dict))
        dict2[i]=copy.deepcopy(all)
    all=[]
print(dict2)
# with open('gdp.json', 'w') as f:
#     json.dump(dict2, f,ensure_ascii=False)  # 会在目录下生成一个1.json的文件，文件内容是dict数据转成的json数据
#


