import time
import re
import requests
from lxml import html
import pymysql as mysql
from multiprocessing.dummy import Pool
from sqlalchemy import create_engine
import pandas as pd
db = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
dbcursor = db.cursor()
hardwaredatalist = []
sqlstr = ""


def getharddata():
    try:
        sql = "select * from cpuhardinfo_clean"
        dbcursor.execute(sql)
        results = dbcursor.fetchall()

        for r in results:
            hardwaredatalist.append(r)
            # hardwaredatalist.append(r[0])

        dbcursor.close()

    except Exception as e:
        print("getharddata error : " + str(e))

def getcompany():
    try:
        for item in hardwaredatalist:
            id = item[0]
            companystr = item[1]
            cleancompany(companystr,id)


    except Exception as e:
        print("getharddata error : " + str(e))


def cleancompany(comstr,tableid):
    number2 = re.findall("[a-zA-Z]+", comstr)
    tagstr = number2[0]
    if(tagstr == 'Intel'):
        try:
            sqlstr = "UPDATE cpuhardinfo_clean SET company = '英特尔' WHERE id = " + str(tableid) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()

        except Exception as e:
            print("cleancompany error : " + str(e))

    if (tagstr == 'AMD'):
        try:
            sqlstr = "UPDATE cpuhardinfo_clean SET company = 'AMD' WHERE id = " + str(tableid) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()

        except Exception as e:
            print("cleancompany error : " + str(e))

    if (tagstr == 'SPARC'):
        try:
            sqlstr = "UPDATE cpuhardinfo_clean SET company = 'SUN' WHERE id = " + str(tableid) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()

        except Exception as e:
            print("cleancompany error : " + str(e))

    if (tagstr == 'UltraSPARC'):
        try:
            sqlstr = "UPDATE cpuhardinfo_clean SET company = 'SUN' WHERE id = " + str(tableid) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()

        except Exception as e:
            print("cleancompany error : " + str(e))

    if (tagstr == 'Power'):
        try:
            sqlstr = "UPDATE cpuhardinfo_clean SET company = 'IBM' WHERE id = " + str(tableid) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()

        except Exception as e:
            print("cleancompany error : " + str(e))

    if (tagstr == 'POWER'):
        try:
            sqlstr = "UPDATE cpuhardinfo_clean SET company = 'IBM' WHERE id = " + str(tableid) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()

        except Exception as e:
            print("cleancompany error : " + str(e))

def getyear():
    try:
        for item in hardwaredatalist:
            id = item[0]
            yearinfo = item[14]
            number1 = re.findall("\d+", yearinfo)  # 输出结果为列表

            sqlstr = "UPDATE cpuhardinfo_clean SET year = '" + str(number1[1]) + "' WHERE id = " + str(id) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()
            #cleancompany(companystr, id)
            test = 1

    except Exception as e:
        print("getyear error : " + str(e))

# 05 = enable 09 = cache
def getmemory():
    try:
        for item in hardwaredatalist:
            id = item[0]
            memoryinfo = item[11]
            number1 = re.findall("\d+", memoryinfo)  # 输出结果为列表
            GBinfo = re.findall("[a-zA-Z]+", memoryinfo)

            memnum = int(number1[0])
            memtype = GBinfo[0]
            if(memtype == "TB"):
                memnum = memnum * 1024

            sqlstr = "UPDATE cpuhardinfo_clean SET memory1 = " + str(memnum) + " WHERE id = " + str(id) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()
            #cleancompany(companystr, id)
            test = 1

    except Exception as e:
        print("getyear error : " + str(e))


def getenabled():
    try:
        for item in hardwaredatalist:
            id = item[0]
            enableinfo = item[5]
            number1 = re.findall("\d+", enableinfo)  # 输出结果为列表
            # GBinfo = re.findall("[a-zA-Z]+", enableinfo)

            enablenum = int(number1[0])
            # memtype = GBinfo[0]


            sqlstr = "UPDATE cpuhardinfo_clean SET enabled1 = " + str(enablenum) + " WHERE id = " + str(id) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()
            #cleancompany(companystr, id)
            test = 1

    except Exception as e:
        print("getyear error : " + str(e))

def getcache():
    try:
        for item in hardwaredatalist:
            id = item[0]
            cacheinfo = item[9]
            number1 = re.findall("\d+", cacheinfo)  # 输出结果为列表
            # GBinfo = re.findall("[a-zA-Z]+", enableinfo)

            cache1 = int(number1[0])
            cache2 = int(number1[1])
            # memtype = GBinfo[0]
            cachenum = cache1 + cache2

            sqlstr = "UPDATE cpuhardinfo_clean SET cache = " + str(cachenum) + " WHERE id = " + str(id) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()
            #cleancompany(companystr, id)
            test = 1
            print("success id == " + str(id))

    except Exception as e:
        print("getcache error : " + str(e))

def main():
    try:
        getharddata()
        # getcompany()
        # getyear()
        # getmemory()
        # getenabled()
        getcache()
    except Exception as e:
        print("Main error : " + str(e))

main()
