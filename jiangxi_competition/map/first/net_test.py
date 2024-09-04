import pandas as pd
import json
import copy
df=pd.read_excel("江西省县级碳排放数据.xlsx")
# print(df)

def fun(year):
    city_flag = df["city"][0]
    data = {}
    dict2 = []
    all_data = []
    for index,value in enumerate(df[year]):#取得2000年的索引和值
        if(city_flag!=df["city"][index]):
            data["name"]=df["city"][index-1]
            all_data.append(copy.deepcopy(data))
            city_flag=df["city"][index]
        dict={"name":df["name"][index],"value":value}
        dict2.append(dict)
        data["children"]=dict2
    all={year:all_data}
    return all

list={}
if __name__ == '__main__':
   year=2000
   for i in range(year,2018):
       data=fun(i)
       print(data)


