import json

import pandas as pd


def cross_Field(crossFiled):
    # crossFiled = ['cond-mat.soft', 'physics.flu-dyn', 'physics.comp-ph', 'physics.ins-det', 'cond-mat.supr-con']
    dataMie = pd.read_json("static/json/mie.json", lines=True)
    df_taxnomy = pd.read_csv("static/json/111.csv")
    crossFiledName = []
    crossFiledClassName = []
    for i in crossFiled:
        crossFiledName.append(df_taxnomy[df_taxnomy['categories'] == i]['category_name'].iloc[0])#全称
        crossFiledClassName.append(df_taxnomy[df_taxnomy['categories'] == i]['group_name'].iloc[0])#所属领域
    crossFiledClassName = list(set(crossFiledClassName))#去重
    # print(crossFiledName)
    # print(crossFiledClassName)
    dataNewMie = {"categories": [], 'nodes': [], 'links': []}
    for i in crossFiledClassName:
        dataNewMie["categories"].append({'name': i})

    crossId = []
    # ids = {}
    id_Number = 0
    for i in dataMie['nodes'][0]:
        if i['name'] in crossFiledName:
            i['category'] = crossFiledClassName.index(i['className'])
            i['id'] = id_Number
            i['symbolSize'] *= 10
            dataNewMie['nodes'].append(i)
            crossId.append(str(i['id']))
            id_Number += 1
    # print(crossId)
    for i in dataMie['links'][0]:
        if i['source'] in crossId and i['target'] in crossId:
            i['source'] = str(crossId.index(i['source']))
            i['target'] = str(crossId.index(i['target']))
            dataNewMie['links'].append(i)
    return dataNewMie
    # print(dataNewMie)


def wordCloudData(name):
    df_taxnomy = pd.read_csv("static/json/111.csv")
    category = df_taxnomy[df_taxnomy['categories'] == name]['category_name'].iloc[0]
    with open('static/json/demo.json', ) as fp:
        words = json.load(fp)

    return_Data = {'data': [], 'name': category}
    for i in words[category]:
        return_Data['data'].append({"name": i[0], "value": i[1]})

    return return_Data
    # print(return_Data)
# wordCloud('cond-mat.soft')
