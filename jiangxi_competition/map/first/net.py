import pandas as pd
import json
import copy
df = pd.read_excel("./data/山东省县级2000-2019年碳排放量.xlsx")
def fun(year):
    df2 = df[["name", "city"]]
    city_flag = df["city"][0]
    data = {}
    dict2 = {}
    arr2 = []
    all_data = []
    for index, value in enumerate(df[year]):#enumerate可获得索引和值
        if (city_flag != copy.deepcopy(df2["city"][index])):
            data["name"] = copy.deepcopy(df2["city"][index - 1])
            all_data.append(copy.deepcopy(data))
            arr2 = []
            city_flag = copy.deepcopy(df2["city"][index])
        dict = {"name": df2["name"][index], "value": value}
        arr2.append(dict)
        data["children"] = arr2
    return  all_data
    # return all

datas={}
if __name__ == '__main__':
   year=2000
   for i in range(year,2018):
       datas[i]=fun(i)
       print(datas)
with open('net.json', 'w') as f:
    json.dump(datas, f,ensure_ascii=False)  # 会在目录下生成一个1.json的文件，文件内容是dict数据转成的json数据




