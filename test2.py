from bs4 import BeautifulSoup  #导入架包
import requests    #导入架包

r=requests.get('https://spec.org/cpu2017/results/res2022q1/') #获取目标网址所有信息
demo=r.text               #定义所有信息的文本
soup=BeautifulSoup(demo,'html.parser')   #BeautifulSoup中的方法
for link in soup.find_all('a'):      #遍历网页中所有的超链接（a标签）
    print(link.get('href'))    #  打印出所有包含href的元素的链接。
