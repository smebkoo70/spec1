from urllib.request import urlopen
from bs4 import BeautifulSoup
# html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

html = urlopen("https://spec.org/cpu2017/results/res2022q1/cpu2017-20211216-30441.html")
# 解析HTML页面；
soup=BeautifulSoup(html)

# hardware
print("Hardwareinfo:")
hardwarelist = soup.findAll("table",{"id":"Hardware"})

for harderware in hardwarelist:
    print(harderware.get_text())

print("Softwareinfo:")
softwarelist = soup.findAll("table",{"id":"Software"})

for softerware in softwarelist:
    print(softerware.get_text())

print("namelist:")
nameList=soup.findAll("table",{"summary":"Detailed per-benchmark result data"})#在soup对象里，findAll函数查找出符合的全部结果，并返回到一个列表中，结果是包含标签及里面的信息；
for name in nameList:
    print(name.get_text())#get_text()使所处理的内容里的标签全部去掉，类似格式化文本输出；

