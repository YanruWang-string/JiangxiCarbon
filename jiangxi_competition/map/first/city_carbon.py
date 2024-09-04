import pandas as pd
import numpy as np
import json
import copy
import collections
loadData=pd.read_excel("1997-2019年城市co2排放量(百万吨).xlsx")
print(loadData)
indicator=loadData.columns[2:].tolist()#获取到1997-2019时间点
city=loadData['城市']
all=[]
dict2={}
dict={}
flag=2000
for i in range(len(indicator)):
    arr=loadData[indicator[i]].tolist()#，每一年各市碳排放
    for j in range(len(arr)):
        dict["name"]=city[j]
        dict["value"]=arr[j]
        all.append(dict)
        dict={}
    dict2[flag]=all
    flag=flag+1
print(dict2)
# with open('carbon1.json', 'w') as f:
#     json.dump(dict2, f,ensure_ascii=False)  # 会在目录下生成一个1.json的文件，文件内容是dict数据转成的json数据




















