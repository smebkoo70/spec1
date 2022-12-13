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
softwaredatalist = []
sqlstr = ""

def getsoftdata():
    try:
        sql = "select * from cpusoftinfo_clean"
        dbcursor.execute(sql)
        results = dbcursor.fetchall()

        for r in results:
            softwaredatalist.append(r)
            # hardwaredatalist.append(r[0])

        dbcursor.close()

    except Exception as e:
        print("getsoftdata error : " + str(e))

# 06 = systemstate 08 = basepointers 10 = peakpointers
def getstate():
    try:
        for item in softwaredatalist:
            id = item[0]
            statenum = 0
            stateinfo = item[6]
            number1 = re.findall("\d+", stateinfo)  # 输出结果为列表
            string2 = re.findall("[a-zA-Z]+", stateinfo)
            if(string2[0] == 'Default'):
                statenum = 1
            else:
                statenum = number1[0]

            sqlstr = "UPDATE cpusoftinfo_clean SET state = '" + str(statenum) + "' WHERE id = " + str(id) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()
            #cleancompany(companystr, id)
            test = 1
            print("update systemstate success! " + str(id))

    except Exception as e:
        print("getstate error : " + str(e))

def getbase():
    try:
        for item in softwaredatalist:
            id = item[0]
            basenum = 0
            baseinfo = item[8]
            number1 = re.findall("\d+", baseinfo)  # 输出结果为列表
            if(len(number1) == 2):
                basenum = 48
            else:
                basenum = number1[0]


            sqlstr = "UPDATE cpusoftinfo_clean SET base = " + str(basenum) + " WHERE id = " + str(id) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()
            # cleancompany(companystr, id)
            test = 1
            print("update basepoint success! " + str(id))

    except Exception as e:
        print("getbasepoint error : " + str(e))


def getpeak():
    try:
        for item in softwaredatalist:
            id = item[0]
            peaknum = 0
            baseinfo = item[10]
            number1 = re.findall("\d+", baseinfo)  # 输出结果为列表
            if(len(number1) == 2):
                peaknum = 48
            if (len(number1) == 0):
                peaknum = 0
            else:
                peaknum = number1[0]


            sqlstr = "UPDATE cpusoftinfo_clean SET peak = " + str(peaknum) + " WHERE id = " + str(id) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()
            # cleancompany(companystr, id)
            test = 1
            print("update peak success! " + str(id))

    except Exception as e:
        print("getpeakpoint error : " + str(e))


def getyear():
    try:
        for item in softwaredatalist:
            id = item[0]
            yearinfo = item[15]
            number1 = re.findall("\d+", yearinfo)  # 输出结果为列表

            sqlstr = "UPDATE cpusoftinfo_clean SET year = '" + str(number1[1]) + "' WHERE id = " + str(id) + ""
            dataconnect = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
            datacursor = dataconnect.cursor()
            datacursor.execute(sqlstr)
            datacursor.close()
            dataconnect.close()
            # cleancompany(companystr, id)
            test = 1
            print("update year success! " + str(id))
    except Exception as e:
        print("getyear error : " + str(e))


def main():
    getsoftdata()
    # getyear()
    getstate()
    getbase()
    getpeak()
main()