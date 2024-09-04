import imp
import json
import random
import geopandas as gp

testData = {"济南": 1.2,"青岛": 0.2,"淄博": 0.5,"枣庄": -0.1,
"东营": -2,"烟台": 2,"潍坊": 5,"济宁": 0.4,"泰安":
 -3,"威海": -0.2,"日照": 1.3,"临沂": 0.2,"德州": -0.2,"聊城":
  -0.5,"滨州": -2,"菏泽": -3}
loadData = gp.read_file("shandong.json")

# print(loadData.name)


loadData['density'] = loadData.name.apply(lambda row: testData[row])
print(loadData)

loadData.to_file("shandongTest.json")