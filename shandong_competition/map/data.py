import pandas as pd
import numpy as np


df1=pd.read_json("shandongnew.json", encoding='utf-8')
df2=pd.read_json("wang.json", encoding='utf-8')
len=df1.__len__()
len2=df2.__len__()
nameArr=[]

for i in range(0,len):
        name=df1["features"][i]['properties']['name']
        coordinates = df1["features"][i]['geometry']['coordinates'][0]
        df2["features"][i]['geometry']['coordinates']=(coordinates)
        df2["features"][i]['properties']['name']=name

arr=np.array([-7.96444334e-02, -6.34055643e-01, -5.44365157e-01,  2.80074772e-03,
        -1.17699517e+00, -3.89425452e-01,  2.80505857e-01, -6.35450713e-01,
        -2.51068078e-01, -1.45904939e-02, -2.28991428e-04,  1.77476005e-01,
        -4.05483689e-01,  8.31282847e-03, -1.69699193e-01, -3.16847849e-03])

len3=arr.__len__()
for i in range(0,len3):
        df2["features"][i]['properties']['density']=arr[i]
df2.drop(labels=range(len,len2),inplace=True)

df2.to_json("wang2.json",)

df=pd.read_json("wang2.json", encoding='utf8')
print(df["features"][0]['properties']['name'])





