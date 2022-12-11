#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 将hardware的内容爬取
import requests
from lxml import html
etree = html.etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
}

# 取得网页源代码
url = f'http://spec.org/cpu2017/results/res2022q1/cpu2017-20211216-30441.html'
response = requests.get(url, headers=headers)
response.encoding = "utf-8"
# print(response.text)

# 解析网页源代码
html = etree.HTML(response.text)
# /html/body/div/div[3]/table[2]/tbody/tr[1]/td
# /html/body/div/div[3]/table[2]/tbody/tr[9]/td
# /html/body/div/div[3]/table[2]/tbody/tr[10]/td

# cell1 = html.xpath('/html/body/div/div[3]/table[1]/tbody/tr[1]/td')[0].text  # CPU Name
# cell2 = html.xpath('/html/body/div/div[3]/table[1]/tbody/tr[2]/td')[0].text  # Max MHz
# print(cell1)
# print(cell2)
softwarelist = list(range(12))
for i in range(1,11):
    softwarelist[i] = html.xpath('/html/body/div/div[3]/table[2]/tbody/tr[' + str(i) +']/td')[0].text

for i in range(1,11):
    print(softwarelist[i])