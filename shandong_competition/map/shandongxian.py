import numpy as np
import pandas as pd
import copy
import json

Data = pd.read_excel("山东.xlsx")
lenth=Data.__len__()
print(Data)
data1={"type":"FeatureCollection","features":[]}
data={"type":"Feature","properties": {},"geometry": {"coordinates":[],"type":"Point"}}
for i in range(lenth):
    copys=copy.deepcopy(data)
    copys["geometry"]["coordinates"]=[Data.iloc[i,3],Data.iloc[i,4]]
    data1["features"].append(copys)#将copys内容加到data1的features中


with open('山东.json', 'w') as json_file:
    json.dump(data1,json_file)

