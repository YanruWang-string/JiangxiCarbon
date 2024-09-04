##爬取OpenStreetMap平台的城市道路交通网数据

import requests
import re

def getCityRpadDataByOSM(cityName):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = '<osm-script><query type="relation"><has-kv k="boundary" v="administrative"/><has-kv k="name:zh" v="'+cityName+'"/></query><print/></osm-script>'
    url = "http://www.overpass-api.de/api/interpreter"
    response = requests.post(url, data = data.encode(), headers = headers)
    # 利用正则表达式提取 id
    match = re.search('<relation id="(.*?)">',response.text)
    id = match.group(1)
    # id 需要 10位
    if id:
        id = str(3600000000+int(id))
        print(id)
    else:
        return
    data2 = '<osm-script timeout="1800" element-limit="100000000"><union><area-query ref="'+id+'"/><recurse type="node-relation" into="rels"/><recurse type="node-way"/><recurse type="way-relation"/></union><union><item/><recurse type="way-node"/></union><print mode="body"/></osm-script>'
    response2 = requests.post(url, data = data2, headers = headers)
    if len(response2.text)>1000:
    # 这里设置阀值是因为 网络问题会导致出现超时，丢掉这个包
        with open(cityName+".osm","w",encoding='utf-8') as f:
            f.write(response2.text)

getCityRpadDataByOSM("济南市")
