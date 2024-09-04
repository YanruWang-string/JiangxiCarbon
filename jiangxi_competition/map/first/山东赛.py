import numpy as np
import pandas as pd
from PyLMDI import PyLMDI

if __name__ == '__main__':
    provinceData = pd.read_excel("1997-2017山东省省级碳排放影响因素数据表.xlsx")
    cityData = pd.read_excel("山东省市级碳排放影响因素.xlsx", sheet_name=None)

    provinceData = np.array(provinceData)
    cityData1 = []
    for i in range(len(cityData)):
        year = 2000 + i
        year = str(year)
        cityData1.append(np.array(cityData[year]))
    cityData2 = []
    for i in range(len(cityData1[0])):
        row = []
        for j in range(len(cityData1)):
            row.append(cityData1[j][i][2:])
        cityData2.append(row)

    cityList = ["济南市", "青岛市", "淄博市", "枣庄市", "东营市", "烟台市", "潍坊市", "济宁市", "泰安市", "威海市", "日照市", "临沂市", "德州市", "聊城市", "滨州市",
                "菏泽市"]
    provinceDataOutPut = []
    cityDataOutPut = []

    # 省级
    for i in range(len(provinceData) - 1):
        # 1998-2020
        Ct = [provinceData[i + 1][1]]
        C0 = [provinceData[i][1]]  # 前一年
        Xt = provinceData[i + 1][2:].reshape([-1, 1])
        X0 = provinceData[i][2:].reshape([-1, 1])  # 前一年
        LMDI = PyLMDI(Ct, C0, Xt, X0)
        ans = LMDI.Add()
        provinceDataOutPut.append(ans[1:])
    provinceDataOutPut = pd.DataFrame(provinceDataOutPut)
    # print(np.shape(provinceData))
    # print(np.shape(provinceDataOutPut))
    #山东省影响因素贡献率
    print(provinceDataOutPut)
    #provinceDataOutPut.to_csv("山东省影响因素贡献率.csv")

    # # 市级
    # for i in range(len(cityData2)):
    #     for j in range(len(cityData2[i]) - 1):
    #         # 2001-2020
    #         Ct = [cityData2[i][j + 1][0]]
    #         C0 = [cityData2[i][j][0]]  # 前一年
    #         Xt = cityData2[i][j + 1][1:].reshape([-1, 1])
    #         X0 = cityData2[i][j][1:].reshape([-1, 1])  # 前一年
    #         LMDI = PyLMDI(Ct, C0, Xt, X0)
    #         ans = LMDI.Add()
    #         cityDataOutPut.append(ans[1:])
    #     cityDataOutPut = pd.DataFrame(cityDataOutPut)
    #     # print(cityDataOutPut)
    #     cityDataOutPut = cityDataOutPut.dropna(axis=1, how="any")
    #     cityDataOutPut.to_csv(str(cityList[i]) + "影响因素贡献率.csv")
    #     cityDataOutPut = []  # 数据清零
    #
    # # 取均值
    # for i in range(len(cityList)):
    #     data = pd.read_csv(str(cityList[i]) + "影响因素贡献率.csv")
    #     data = np.array(data)
    #     bardata = []
    #     for j in range(4):
    #         row = data[4 * j] / 5 + data[4 * j + 1] / 5 + data[4 * j + 2] / 5 + data[4 * j + 3] / 5 + data[4 * j + 4] / 5
    #         bardata.append(row[1:])
    #     bardata = pd.DataFrame(bardata)
    #     bardata.to_csv(str(cityList[i]) + "data.csv")
    #
