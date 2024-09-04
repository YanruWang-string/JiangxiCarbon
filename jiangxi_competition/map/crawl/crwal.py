from selenium import webdriver
import datetime
from dateutil.relativedelta import relativedelta
from lxml import etree
import pandas as pd
import os
import json
from selenium.webdriver.common.by import By
import random
from urllib.request import urlopen
import urllib.request
import urllib.error
# import execjs
from urllib.request import urlopen
# 全局取消证书验证
import ssl
"""
爬取网址: http://lishi.tianqi.com
"""
import requests
import re
import time
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

startYear = 2022
endYear = 2022


def YqData():
    # 通过url获取数据
    def get_page(url):
        # requests.get 自带 json.load
        page = requests.get(url)
        page = page.content
        # 将bytes转换成字符串
        page = page.decode('utf-8')
        return page

    def get_json():
        """
         xiaolanzao, 2022.02.27
        【作用】
         读取本地文件，获取json信息
        【参数】
         无
        【返回】
         json字符串
        """
        # 读取本地文件
        f = open("data/疫情数据/疫情数据.txt", "r", encoding="utf-8")
        f_content = f.read()
        f.close()


        # json字符串前后关键词
        json_start = "try { window.getAreaStat = "
        # 字符串包含的括号要进行转义
        json_end = "}catch\(e\){}"

        # json字符串正则匹配
        # (.*?)是匹配所有内容
        regular_key = json_start + "(.*?)" + json_end
        # 参数rs.S可以无视换行符，将所有文本视作一个整体进行匹配
        re_content = re.search(regular_key, f_content, re.S)
        # group()用于获取正则匹配后的字符串
        content = re_content.group()

        # 去除json字符串的前后关键词
        content = content.replace(json_start, '')
        # 尾巴要去掉转义符号
        json_end = "}catch(e){}"
        content = content.replace(json_end, '')
        return content

    def dxy_data_down(article_url):
        url = urlopen(article_url)
        soup = BeautifulSoup(url, 'html.parser')  # parser解析
        f = open("data/疫情数据/疫情数据.txt", "w", encoding="utf-8")
        f.write(str(soup))
        f.close()

    def mkdir(path):
        """
        :param path: 创建文件夹位置
        :return:
        """
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            os.makedirs(path)
            return False
        return True

    def yiqing():
        dxy_data_down("https://ncov.dxy.cn/ncovh5/view/pneumonia")
        # json字符串前后关键词
        json_start = "try { window.getAreaStat = "
        # 字符串包含的括号要进行转义
        json_end = "}catch\(e\){}"
        # json字符串正则匹配
        # (.*?)是匹配所有内容
        regular_key = json_start + "(.*?)" + json_end
        json_content = get_json()

        def display_provinces(json_content, province_name):
            json_data = json.loads(json_content)
            for i in json_data:
                if i["provinceName"] == province_name:
                    # 读取里面的城市信息
                    try:
                        return i['statisticsData']
                    except:
                        return "没有信息啊！！！"

        mkdir('data/疫情数据')
        # 爬取山东整体疫情发展
        data = pd.DataFrame(json.loads(get_page(display_provinces(json_content, "山东省")))['data'])
        data.to_csv('data/疫情数据/allYQ.csv', index=0)
        # 爬取山东各市区疫情发展情况
        priUrl = 'https://c.m.163.com/ug/api/wuhan/app/data/list-by-area-code?areaCode='
        my_headers = [
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
        ]

        # 破解反爬
        def get_content2(url, headers):
            '''
            @获取403禁止访问的网页
            '''
            randdom_header = random.choice(headers)

            req = urllib.request.Request(url)
            req.add_header("User-Agent", randdom_header)
            req.add_header("Host", "blog.csdn.net")
            req.add_header("Referer", "http://blog.csdn.net/")
            req.add_header("GET", url)
            content = urllib.request.urlopen(req).read()
            return content

        # 获取城市名和行政区划
        data = pd.read_csv('./cityInfor.csv')
        city = list(data['城市'])
        codes = list(data['行政代码'])
        s = []
        for i in range(len(city)):
            try:
                data = pd.DataFrame(json.loads(
                    get_content2(
                        priUrl + str(codes[i]),
                        my_headers
                    )
                )['data']['list'])
                dates = list(data['date'])
                todays = list(data['today'])
                totals = list(data['total'])
                for ii in range(len(dates)):
                    _s = {}

                    def appd(header, value):
                        try:
                            _s.update({
                                header: int(value),
                            })
                        except:
                            _s.update({
                                header: 0,
                            })

                    _s.update({
                        "日期": dates[ii]
                    })
                    _s.update({
                        "城市": city[i]
                    })
                    appd("确诊", todays[ii]['confirm'])
                    appd("疑似", todays[ii]['suspect'])
                    appd("治愈", todays[ii]['heal'])
                    appd("死亡", todays[ii]['dead'])
                    appd("累计确诊", totals[ii]['confirm'])
                    appd("累计疑似", totals[ii]['suspect'])
                    appd("累计治愈", totals[ii]['heal'])
                    appd("累计死亡", totals[ii]['dead'])
                    s.append(_s)
            except:
                print(city[i], "没有")
        pd.DataFrame(s).to_csv(
            './qydata.csv',
            index=0
        )

    yiqing()

    print('疫情数据爬取完成')


def WrData():
    # 反反爬
    options = webdriver.ChromeOptions()
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome = webdriver.Chrome(options=options)
    chrome.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })

    def get_order(chrome):
        res = chrome.execute_script('return ' + re.findall('eval\((.+)\)', chrome.page_source)[-1])  # 得到eval结果
        id_str, res = \
            re.findall('items.forEach\(function\(item\) {[\s\S]*?\$\(\'#(\w+) tbody\'\)\.append\(([\s\S]+?)\);', res)[
                0]  # 粗略结果
        res = re.findall('<td.+?</td>', res)
        order = []
        attr2col = {
            'time_point': '日期',
            'aqi': 'AQI',
            'quality': '质量等级',
            'pm2_5': 'PM2.5',
            'pm10': 'PM10',
            'so2': 'SO2',
            'co': 'CO',
            'no2': 'NO2',
            'o3': 'O3'
        }
        for td in res:
            col = re.findall('item\.(\w+) +', td)
            if col:
                order.append(attr2col[col[0]])
            else:
                order.append('')
        return id_str, order

    def export(chrome, city, datas):
        id_str, order = get_order(chrome)
        html = etree.HTML(chrome.page_source)
        data_all = {}
        for tr in html.xpath(f'.//table[@id="{id_str}"]')[0].xpath('.//tr')[1:]:
            data = []
            for td in tr.xpath('./td'):
                if td.xpath('./span'):
                    data.append(td.xpath('./span/text()')[0])
                else:
                    data.append(td.xpath('./text()')[0])
            for col, value in zip(order, data):
                if col:
                    if col not in data_all:
                        data_all[col] = []
                    data_all[col].append(value)
        df = pd.DataFrame(data_all)
        df['城市'] = city
        return pd.concat([datas, df], axis=0, ignore_index=True)

    datas = pd.DataFrame()
    citys = list(pd.read_csv('./cityInfor.csv')['城市'])
    for city in citys:
        base_url = 'https://www.aqistudy.cn/historydata/daydata.php?city=' + city + '&month={}'
        start_day = datetime.datetime(startYear, 1, 1)  # 设置开始时间
        end_day = datetime.datetime(endYear, 12, 31)
        day = start_day
        while day <= end_day:
            dayStr = datetime.datetime.strftime(day, '%Y%m')
            url = base_url.format(dayStr)
            chrome.get(url)
            while len(chrome.find_elements(By.XPATH,'.//table')) != 3: pass
            time.sleep(3)
            datas = export(chrome, city, datas)
            day += relativedelta(months=1)
    datas.to_csv('AQIdata.csv', index=0)
    print("污染数据爬取完成")


def QxData():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Cookie': 'lianjia_uuid=9d3277d3-58e4-440e-bade-5069cb5203a4; UM_distinctid=16ba37f7160390-05f17711c11c3e-454c0b2b-100200-16ba37f716618b; _smt_uid=5d176c66.5119839a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ba37f7a942a6-0671dfdde0398a-454c0b2b-1049088-16ba37f7a95409%22%2C%22%24device_id%22%3A%2216ba37f7a942a6-0671dfdde0398a-454c0b2b-1049088-16ba37f7a95409%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.1772719071.1561816174; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1561822858; _jzqa=1.2532744094467475000.1561816167.1561822858.1561870561.3; CNZZDATA1253477573=987273979-1561811144-%7C1561865554; CNZZDATA1254525948=879163647-1561815364-%7C1561869382; CNZZDATA1255633284=1986996647-1561812900-%7C1561866923; CNZZDATA1255604082=891570058-1561813905-%7C1561866148; _qzja=1.1577983579.1561816168942.1561822857520.1561870561449.1561870561449.1561870847908.0.0.0.7.3; select_city=110000; lianjia_ssid=4e1fa281-1ebf-e1c1-ac56-32b3ec83f7ca; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMzQ2MDU5ZTQ0OWY4N2RiOTE4NjQ5YmQ0ZGRlMDAyZmFhODZmNjI1ZDQyNWU0OGQ3MjE3Yzk5NzFiYTY4ODM4ZThiZDNhZjliNGU4ODM4M2M3ODZhNDNiNjM1NzMzNjQ4ODY3MWVhMWFmNzFjMDVmMDY4NWMyMTM3MjIxYjBmYzhkYWE1MzIyNzFlOGMyOWFiYmQwZjBjYjcyNmIwOWEwYTNlMTY2MDI1NjkyOTBkNjQ1ZDkwNGM5ZDhkYTIyODU0ZmQzZjhjODhlNGQ1NGRkZTA0ZTBlZDFiNmIxOTE2YmU1NTIxNzhhMGQ3Yzk0ZjQ4NDBlZWI0YjlhYzFiYmJlZjJlNDQ5MDdlNzcxMzAwMmM1ODBlZDJkNmIwZmY0NDAwYmQxNjNjZDlhNmJkNDk3NGMzOTQxNTdkYjZlMjJkYjAxYjIzNjdmYzhiNzMxZDA1MGJlNjBmNzQxMTZjNDIzNFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIzMGJlNDJiN1wifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL3p1ZmFuZy9yY28zMS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='
    }
    date_box = []
    max_temp = []
    min_temp = []
    weh = []
    wind = []
    week_box = []
    citys = []
    cityList = list(pd.read_csv('./cityInfor.csv')['城市拼音'])
    cityName = list(pd.read_csv('./cityInfor.csv')['城市'])

    def set_link(year, city):
        # year参数为需要爬取数据的年份
        link = []
        for i in range(1, 13):
            # 一年有12个月份
            if i < 10:
                url = 'http://lishi.tianqi.com/' + city + '/{}0{}.html'.format(year, i)
            else:
                url = 'http://lishi.tianqi.com/' + city + '/{}{}.html'.format(year, i)
            link.append(url)
        return link

    def get_page(url, headers):
        html = requests.get(url, headers=headers)
        if html.status_code == 200:
            html.encoding = html.apparent_encoding
            return html.text
        else:
            return None

    def get_data(index):
        for year in range(startYear, endYear + 1):
            link = set_link(int(year), cityList[index])
            for url in link:
                try:
                    html = get_page(url, headers)
                    bs = BeautifulSoup(html, 'html.parser')
                except:
                    r = requests.get(url)
                    c = r.content
                    bs = BeautifulSoup(c, "html.parser")
                data = bs.find_all(class_='thrui')
                date = re.compile('class="th200">(.*?)</')
                tem = re.compile('class="th140">(.*?)</')
                time = re.findall(date, str(data))
                for item in time:
                    week = item[10:]
                    week_box.append(week)
                    date_box.append(item[:10])
                temp = re.findall(tem, str(data))
                for i in range(len(time)):
                    max_temp.append(temp[i * 4 + 0])
                    min_temp.append(temp[i * 4 + 1])
                    weh.append(temp[i * 4 + 2])
                    wind.append(temp[i * 4 + 3])
                    citys.append(cityName[index])
    for i in range(len(cityList)):
        get_data(i)

    datas = pd.DataFrame(
        {'日期': date_box, '星期': week_box, '最高温度': max_temp, '最低温度': min_temp, '天气': weh, '风向': wind, '城市': citys})
    datas.to_csv('./weather.csv', encoding='utf_8_sig', index=0)
    print('气象数据爬取完成')


# YqData()
QxData()
WrData()
