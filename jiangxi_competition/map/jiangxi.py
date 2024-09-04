import csv
import imp
import json
import random
import geopandas as gp
import pandas as pd


testData = {}
with open('2012LISA.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name = row[0]
        value = row[2]
        testData[name] = value
print(testData)



# testData = {'济南': 'LH','青岛': 'LL'}

loadData = gp.read_file("2011.json")

#print(loadData.name)

loadData['density'] = loadData.name.apply(lambda row: testData[row])#新加density字段，apply为读取每一个元素，这里读取的是name下面的row字段
print(loadData)
loadData.to_file("shang2012.json")