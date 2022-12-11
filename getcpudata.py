#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 将hardware的内容爬取
import requests
from lxml import html
import pymysql as mysql
from multiprocessing.dummy import Pool
from sqlalchemy import create_engine
import pandas as pd
db = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
dbcursor = db.cursor()


etree = html.etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
}


def query(url):
    requests.get(url)

pool = Pool(5)

def gethard(htmllist = []):

    # url = ""
    # 取得网页源代码

    for childhtml in htmllist:
        try:
            url = childhtml
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
                hardwarelist[i] = html.xpath('/html/body/div/div[3]/table[1]/tbody/tr[' + str(i+1) + ']/td')[0].text
            MySQLhard(url,hardwarelist)


        except Exception as e:
            print("gethard " + str(e))

    #url = f'http://spec.org/cpu2017/results/res2022q1/cpu2017-20211216-30441.html'

sql1 = "123456"

def MySQLhard(url1,hardinfo = []):
    sql1 = "INSERT INTO cpuhardinfo (cpuname, maxmhz, nominal, enabled, orderable, cachel1, l2, l3, cacheother, memory, storage, other, htmlpath) VALUES ('" + str(
        hardinfo[0]) + "','" + str(hardinfo[1]) + "','" + str(hardinfo[2]) + "','" + str(hardinfo[3]) + "','" + str(
        hardinfo[4]) + "','" + str(hardinfo[5]) + "','" + str(hardinfo[6]) + "','" + str(hardinfo[7]) + "','" + str(
        hardinfo[8]) + "','" + str(hardinfo[9]) + "','" + str(hardinfo[10]) + "','" + str(hardinfo[11]) + "','" + url1 + "')"
    cnt = 0
    try:
        # sql = "INSERT INTO cpuhardinfo ('cpuname', 'maxmhz', 'nominal', 'enabled', 'orderable', 'cachel1', 'l2', 'l3', 'cacheother', 'memory', 'storage', 'other') VALUES (''" + str(hardinfo[0]) + "','" +  hardinfo[1] + "','" +  hardinfo[2]  + "','" +  hardinfo[3] + "','" +  hardinfo[4] + "','" +  hardinfo[5]  + "','" +  hardinfo[6]  + "','" +  hardinfo[7]  + "','" +  hardinfo[8]  + "','" +  hardinfo[9]  + "','" +  hardinfo[10]  + "','" +  hardinfo[11] + "')'"
        # sql1 = "INSERT INTO cpuhardinfo ('cpuname', 'maxmhz', 'nominal', 'enabled', 'orderable', 'cachel1', 'l2', 'l3', 'cacheother', 'memory', 'storage', 'other') VALUES (''" + str(hardinfo[0]) + "','" +  str(hardinfo[1]) + "','" +  str(hardinfo[2])  + "','" +  str(hardinfo[3]) + "','" +  str(hardinfo[4]) + "','" +  str(hardinfo[5])  + "','" +  str(hardinfo[6])  + "','" +  str(hardinfo[7])  + "','" +  str(hardinfo[8])  + "','" +  str(hardinfo[9])  + "','" + str(hardinfo[10])  + "','" +  str(hardinfo[11]) + "')'"

        dbcursor.execute(sql1)

        print("insert info success!" + str(cnt))
        cnt = cnt + 1

    except Exception as e:
        print("mysqlhard " + str(e))


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
            htmldatalist.append(r[0])

        listlen = len(htmldatalist)
        gethard(htmldatalist)

        # writeevent.
        # db.commit()
        # datanum + 1

    except Exception as e:
        print("gethtmlpath " + str(e))


def main():
    gethtmlpath()


main()