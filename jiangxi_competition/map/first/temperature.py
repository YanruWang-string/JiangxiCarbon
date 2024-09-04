import pandas as pd
import numpy as np
import json
import copy

list1 = {"list": {}}
Data1 = pd.read_excel("./data/山东省2000-2020各市历年温度数据.xlsx",sheet_name="Sheet1")
Data2 = pd.read_excel("./data/山东省2000-2019市级碳排放数据.xlsx",sheet_name="Sheet1")
print(Data1)
print(Data2)


def drawData1(row):
    #print(row)
    list1['list'][row['city']] = {}
    list1['list'][row['city']]['data1'] = row.tolist()[1:]#取第一个到最后一个数据(14.5),从一个字典第一个数取到最后一个
def drawData2(row):
    list1['list'][row['city']]['data2'] = row.tolist()[1:]
Data1.apply(drawData1, axis=1)#axis=1把每一行拿出来做for循环
Data2.apply(drawData2,axis=1)
print(json.dumps(list1,ensure_ascii=False))

