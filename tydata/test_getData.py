import requests
from bs4 import BeautifulSoup
import selenium
from data_class import CPU
import re
from pymysql import Connection

from data_class.CPU import Test_CPURates, Test_CPUSpeed


def getMysqlCon() -> Connection:
    return Connection(
        host='localhost',
        port=3306,
        user='root',
        password='qwerdf521',
        database='datacontro',
        autocommit=True
    )


def insertRateMysql(rates: Test_CPURates):
    con = getMysqlCon()
    cursor = con.cursor()
    sql = "insert into cpu_rate values (null,'{0}',{1},{2},{3},{4},'{5}','{6}','{7}')".format(rates.sys_name, rates.base_copies,
                                                                                      rates.enable_cores,
                                                                                      rates.enable_chip,
                                                                                      rates.thread_core, rates.base,
                                                                                      rates.peak, '1')
    cursor.execute(sql)
    con.close()


def insertSpeedMysql(speed: Test_CPUSpeed):
    con = getMysqlCon()
    cursor = con.cursor()
    sql = "insert into cpu_speed values (null,'{0}',{1},{2},{3},{4},'{5}','{6}','{7}','{8}')".format(speed.sys_name,
                                                                                          speed.base_threads,
                                                                                          speed.enable_cores,
                                                                                          speed.enable_chip,
                                                                                          speed.thread_core, speed.base,
                                                                                          speed.peak, '1',
                                                                                          speed.parallel)
    cursor.execute(sql)
    con.close()


def getDataFromUrl(url: str):
    # url = "https://spec.org/cpu2017/results/res2022q1/"
    resData = requests.get(url)
    soup = BeautifulSoup(resData.text, 'html.parser')
    resList = []
    resList2 = []
    divs = soup.find_all('div')
    for div in divs:
        if 'class' in div.attrs:
            if div['class'][0] == "idx_table":
                h2 = div.find('h2')
                test_name = h2.a.string
                print(test_name)
                if 'Rates' in test_name:
                    tBody = div.find('tbody')
                    trs = tBody.find_all('tr')
                    for tr in trs:
                        data = Test_CPURates()
                        if 'class' not in tr.attrs or 'header' not in tr['class']:
                            tds = tr.find_all('td')
                            for td in tds:
                                if 'hw_model' in td['class']:
                                    data.setSys_name(td.contents[0])
                                    continue
                                if 'base_copies' in td['class']:
                                    # print(td.string)
                                    data.setBase_copies(int(td.string))
                                    continue
                                if 'hw_ncores' in td['class']:
                                    data.setEnable_cores(int(td.string))
                                    continue
                                if 'hw_nchips' in td['class']:
                                    data.setEnable_chip(int(td.string))
                                    continue
                                if 'hw_nthreadspercore' in td['class']:
                                    # print(td.string)
                                    data.setThread_core(int(td.string))

                                    continue
                                if 'basemean' in td['class']:
                                    # print(td.string)
                                    data.setBase(td.string)
                                    continue
                                if 'peakmean' in td['class']:
                                    # print(td.string)
                                    data.setPeak(td.string)
                            resList.append(data)
                    for i in resList:
                        print(i)
                        # insertRateMysql(i)
                    continue
                if 'Speed' in test_name:
                    tbody = div.find('tbody')
                    trs = tbody.find_all('tr')
                    for tr in trs:
                        if 'class' not in tr.attrs or 'header' not in tr['class']:
                            data = Test_CPUSpeed()
                            tds = tr.find_all('td')
                            for td in tds:
                                if 'hw_model' in td['class']:
                                    data.setSys_name(td.contents[0])
                                    continue
                                if 'sw_parallel' in td['class']:
                                    data.setParallel(td.string)

                                if 'base_thread' in td['class']:
                                    # print(td.string)
                                    data.setBase_threads(int(td.string))
                                    continue
                                if 'hw_ncores' in td['class']:
                                    data.setEnable_cores(int(td.string))
                                    continue
                                if 'hw_nchips' in td['class']:
                                    data.setEnable_chip(int(td.string))
                                    continue
                                if 'hw_nthreadspercore' in td['class']:
                                    # print(td.string)
                                    data.setThread_core(int(td.string))

                                    continue
                                if 'basemean' in td['class']:
                                    # print(td.string)
                                    data.setBase(td.string)
                                    continue
                                if 'peakmean' in td['class']:
                                    data.setPeak(td.string)
                            resList2.append(data)
                    for i in resList2:
                        insertSpeedMysql(i)


getDataFromUrl('https://spec.org/cpu2017/results/res2022q1/')
