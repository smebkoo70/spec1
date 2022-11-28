#未从初始位置匹配，会返回None
import re

import requests
from bs4 import BeautifulSoup
import bs4

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.text)
        return r.text
    except:
        return ""





def fillUniverList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")

    for tr in soup.tbody.children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].text.strip(), tds[1].text.strip(), tds[3].text.strip()])


def printUniverList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))


def main():
    uinfo = []
    #url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    url = 'https://www.shanghairanking.cn/rankings/bcur/2022'
    html = getHtmlText(url)
    fillUniverList(uinfo, html)
    printUniverList(uinfo, 40)


line = 'i can speak good english'
matchObj = re.match(r'(i)\s(\w*)\s(\w*).*',line)
if matchObj:
   print('matchObj.group() :',matchObj.group())
   print('matchObj.group() :',matchObj.group(1))
   print('matchObj.group() :',matchObj.group(2))
   print('matchObj.group() :',matchObj.group(3))
else:
   print('no match!')
