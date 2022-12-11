#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 将hardware的内容爬取
import time

import requests
from lxml import html
import pymysql as mysql
from multiprocessing.dummy import Pool
from sqlalchemy import create_engine
import pandas as pd
db = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
dbcursor = db.cursor()
url_list = []
etree = html.etree

cnt = 0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
}

# 自定义函数,实现多线程爬虫，但是保证不了数据顺序了，没办法。
def query(url):
    try:
        requests.get(url)
        response = requests.get(url, headers=headers)
        response.encoding = "utf-8"
        # print(response.text)

        # 解析网页源代码
        html = etree.HTML(response.text)
        # cell1 = html.xpath('/html/body/div/div[3]/table[1]/tbody/tr[1]/td')[0].text  # CPU Name
        # cell2 = html.xpath('/html/body/div/div[3]/table[1]/tbody/tr[2]/td')[0].text  # Max MHz
        # print(cell1)
        # print(cell2)
        hardwarelist = list(range(15))
        for i in range(0, 12):
            hardwarelist[i] = html.xpath('/html/body/div/div[3]/table[1]/tbody/tr[' + str(i + 1) + ']/td')[0].text
        MySQLhard(url, cnt, hardwarelist)
    except Exception as e:
        print("queryerror: " + str(e))



def gethtmlpath():
    try:
        sql = "select * from htmlpath2017"
        # engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/spec')
        # df_read = pd.read_sql_query(sql, engine)

        # print(df_read)
        dbcursor.execute(sql)
        #dbcursor.execute(sql)
        results = dbcursor.fetchall()
        htmldatalist = []
        for r in results:
            url_list.append(r[0])

        listlen = len(htmldatalist)
        # gethard(htmldatalist)

        # writeevent.
        # db.commit()
        # datanum + 1

    except Exception as e:
        print("gethtmlpath " + str(e))

sql1 = "123456"

def MySQLhard(url1, cnt1, hardinfo = []):
    sql1 = "INSERT INTO cpuhardinfo (cpuname, maxmhz, nominal, enabled, orderable, cachel1, l2, l3, cacheother, memory, storage, other, htmlpath) VALUES ('" + str(
        hardinfo[0]) + "','" + str(hardinfo[1]) + "','" + str(hardinfo[2]) + "','" + str(hardinfo[3]) + "','" + str(
        hardinfo[4]) + "','" + str(hardinfo[5]) + "','" + str(hardinfo[6]) + "','" + str(hardinfo[7]) + "','" + str(
        hardinfo[8]) + "','" + str(hardinfo[9]) + "','" + str(hardinfo[10]) + "','" + str(hardinfo[11]) + "','" + url1 + "')"

    try:
        # sql = "INSERT INTO cpuhardinfo ('cpuname', 'maxmhz', 'nominal', 'enabled', 'orderable', 'cachel1', 'l2', 'l3', 'cacheother', 'memory', 'storage', 'other') VALUES (''" + str(hardinfo[0]) + "','" +  hardinfo[1] + "','" +  hardinfo[2]  + "','" +  hardinfo[3] + "','" +  hardinfo[4] + "','" +  hardinfo[5]  + "','" +  hardinfo[6]  + "','" +  hardinfo[7]  + "','" +  hardinfo[8]  + "','" +  hardinfo[9]  + "','" +  hardinfo[10]  + "','" +  hardinfo[11] + "')'"
        # sql1 = "INSERT INTO cpuhardinfo ('cpuname', 'maxmhz', 'nominal', 'enabled', 'orderable', 'cachel1', 'l2', 'l3', 'cacheother', 'memory', 'storage', 'other') VALUES (''" + str(hardinfo[0]) + "','" +  str(hardinfo[1]) + "','" +  str(hardinfo[2])  + "','" +  str(hardinfo[3]) + "','" +  str(hardinfo[4]) + "','" +  str(hardinfo[5])  + "','" +  str(hardinfo[6])  + "','" +  str(hardinfo[7])  + "','" +  str(hardinfo[8])  + "','" +  str(hardinfo[9])  + "','" + str(hardinfo[10])  + "','" +  str(hardinfo[11]) + "')'"
        # cnt1++
        dbcursor.execute(sql1)
        cnt1 += 1
        # cnt = cnt1
        # print("insert info success!" + " " + str(cnt1))
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


    except Exception as e:
        print("mysqlhard " + str(e))





def main():
    cnt = 0
    gethtmlpath()
    pool = Pool(10)
    pool.map(query, url_list)

main()