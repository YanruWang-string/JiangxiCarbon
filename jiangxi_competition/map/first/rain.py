import pandas as pd
import numpy as np
import json
import copy
AllData=pd.read_excel("./data/山东省2000-2019各市降水.xlsx")
dict=[]
dict2=[]
indicator=AllData.columns[1:].tolist()#获取到1997-2019时间点
print(indicator)
for i in indicator:
    arr=AllData[i].tolist()
    print(arr)
    for j in range(len(arr)):
        dict=[]
        dict.append(str(i)+'/1/1')
        dict.append(arr[j])
        dict.append(AllData['city'][j])
        print(dict)
        dict2.append(copy.deepcopy(dict))
print(dict2)
with open('rain.json', 'w') as f:
    json.dump(dict2, f,ensure_ascii=False)  # 会在目录下生成一个1.json的文件，文件内容是dict数据转成的json数据
