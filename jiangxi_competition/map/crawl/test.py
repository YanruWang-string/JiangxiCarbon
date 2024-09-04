import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://lishi.tianqi.com/baishui/202210.html"

headers = {
    'User-Agent': "PostmanRuntime/7.16.3",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "lishi.tianqi.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
lishitable = soup.find("div", {"class": "tian_three"})
lishitable_content = lishitable.find("ul")
# lishitable_content1 = lishitable_content[1]
data_all = []
lishi_li = lishitable_content.find_all("li")
for i in lishi_li:
    lishi_div = i.find_all("div")
    data = []
    for j in lishi_div:
        data.append(j.text)
    data_all.append(data)
weather = pd.DataFrame(data_all)
weather.columns = ["日期", "最高气温", "最低气温", "天气", "风向"]
weather_shape = weather.shape
weather.drop((weather_shape[0] - 1), inplace=True)
weather.to_csv("test.csv", encoding="utf_8_sig")