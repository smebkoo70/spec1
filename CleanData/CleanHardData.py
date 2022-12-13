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

def main():
    try:
        getharddata()
        # getcompany()
        # getyear()
    except Exception as e:
        print("Main error : " + str(e))

main()
