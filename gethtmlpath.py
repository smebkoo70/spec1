# /html/body/div[2]/table/tbody/tr[1]/td[2]/span/a[1]
# /html/body/div[2]/table/tbody/tr[13]/td[2]/span/a[1]
# /html/body/div[2]/table/tbody/tr[16]/td[2]/span/a[1]
# /html/body/div[2]/table/tbody/tr[28]/td[2]/span/a[1]
# /html/body/div[2]/table/tbody/tr[258]/td[2]/span/a[1]

# /html/body/div[3]/table/tbody/tr[1]/td[2]/span/a[1]
#

# /html/body/div[5]/table/tbody/tr[191]/td[2]/span/a[1]

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
url = f'https://spec.org/cpu2017/results/res2022q1/'
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
htmllist1 = list(range(260))
j = 1

for i in range(1, 260):
    try:
        htmllist1[j] = html.xpath('/html/body/div[2]/table/tbody/tr[' + str(i) + ']/td[2]/span/a[1]/@href')[0]
        # print("i == " + str(i) + " j == " + str(j) + " " + htmllist1[j])
        j = j + 1

    except:
        pass
        # print("i == " + str(i) + " j == " + str(j))

    else:
        pass



print()

for it in range(1, 225):
    print(str(it) + " == " + htmllist1[it])


htmllist2 = list(range(260))
j = 1

for i in range(1, 260):
    try:
        htmllist2[j] = html.xpath('/html/body/div[3]/table/tbody/tr[' + str(i) + ']/td[2]/span/a[1]/@href')[0]
        # print("i == " + str(i) + " j == " + str(j) + " " + htmllist1[j])
        j = j + 1

    except:
        pass
        # print("i == " + str(i) + " j == " + str(j))

    else:
        pass



print()

for it in range(1, 159):
    print(str(it) + " == " + htmllist2[it])