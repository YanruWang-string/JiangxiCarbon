import pandas as pd
import numpy as np
import json
import copy
import geopandas as gp
loadData=pd.read_excel("全国经纬度和adcode.xlsx")
print(loadData)

data={"list":{}}
for i in range(len(loadData)):
    data['list'][loadData.iloc[i,1]] =  [loadData.iloc[i, 3], loadData.iloc[i, 4]]
print(data)
with open('carbon.json', 'w') as f:
    json.dump(data, f,ensure_ascii=False)  # 会在目录下生成一个1.json的文件，文件内容是dict数据转成的json数据