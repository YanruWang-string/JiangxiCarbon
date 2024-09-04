import imp
import json
import pandas as pd
import copy
import numpy as np
import random
import xlrd
#import geopandas as gp
#分行业碳排放数据

datadict={"name":[],"type":"line","xAxisIndex": 1,"yAxisIndex": 1,"symbolSize": 3,"hoverAnimation": "false","data": []}#确定格式
datas={"list":[]}
LoadData=pd.read_json("江苏省分行业碳排放数据.json")
LoadData.rename(columns = {0:"time",1:'value',2:"city"}, inplace=True)#增加索引
LoadData['time'] = pd.to_datetime(LoadData['time'],format='%Y-%m-%d')#因为要按时间排序所以要重新设置时间格式
classes = LoadData.iloc[:,2].tolist()#转成list
#print(classes)
classes_dump = list(set(classes))#去重
#print(classes_dump)

for i in classes_dump:
    alldata = LoadData[LoadData['city']==i]#筛选
    alldata.sort_values(by='time',inplace=True,ascending=True)#按time排序
    #print(alldata)
    datadict["name"]=i
    #print(datadict)
    datadict["data"]=alldata["value"].tolist()
    #print(datadict["data"])
    #print(datadict)
    datas['list'].append(copy.deepcopy(datadict))#如果不写深拷贝的话就只有一行数据



with open('hangye_new.json', 'w') as f:
    json.dump(datas, f, ensure_ascii=False)  # 会在目录下生成一个1.json的文件，文件内容是dict数据转成的json数据















