import json
import pandas as pd
import copy
import numpy as np
import random
import xlrd
#import geopandas as gp
#添加字段
data = {"type": "FeatureCollection","features":[]}
dicts ={"geometry":{"coordinates":[],"type":"Point"},"properties":{},"type":"Feature"}
loadData = pd.read_excel("山东县.xlsx")
for i in range(len(loadData)):
    dict_copy =  copy.deepcopy(dicts)#copy.deepcopy深拷贝，完全拷贝了父对象及其子对象。   copy.copy不会拷贝对象的内部的子对象。
    # dict_copy["geometry"]["coordinates"] = [loadData.iloc[i,3],loadData.iloc[i,4]]#loadData.iloc[i,3]提取第三列的第i行所有数据
    dict_copy["geometry"]["coordinates"] = list(map(float,loadData.iloc[i,2].split("，")[:2]))#loadData.iloc[i,3]提取第三列的第i行所有数据
    data["features"].append(dict_copy)

with open('dict1.json', 'w') as f:
     json.dump(data, f)  # 会在目录下生成一个1.json的文件，文件内容是dict数据转成的json数据

# data.("jiangxixian.json")