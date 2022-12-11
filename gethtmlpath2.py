import requests
from lxml import html

import pymysql as mysql
db = mysql.connect(host="localhost", port=3306, user="root", passwd="", db="spec")
dbcursor = db.cursor()
datanum = 0

etree = html.etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
}


def gethtmlinfo(url):
    # url = f'https://spec.org/cpu2017/results/res2022q1/'
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    # print(response.text)

    # 解析网页源代码
    html = etree.HTML(response.text)
    getpath(url,html)
    getpath2(url,html)
    getpath3(url, html)
    getpath4(url, html)


# /html/body/div[2]/table/tbody/tr[1]/td[2]/span/a[1]
# /html/body/div[2]/table/tbody/tr[477]/td[2]/span/a[1]
def getpath(url,html):

    htmllist = list(range(2005))
    j = 1
    # xpath1
    strfront = '/html/body/div[5]/table/tbody/tr['
    print("url == " + str(url))
    for i in range(1, 2005):
        try:
            htmllist[j] = html.xpath('/html/body/div[2]/table/tbody/tr[' + str(i) + ']/td[2]/span/a[1]/@href')[0]
            urlstr = str(url)
            htmlxpath = urlstr + htmllist[j]
            WriteToMySQL(htmlxpath)
            # print("htmlxpath == " + htmlxpath)
            # print("i == " + str(i) + " j == " + str(j) + " " + htmllist[j])
            j = j + 1

        except:
            pass
            # print("i == " + str(i) + " j == " + str(j))

        else:
            pass

def getpath2(url,html):

    htmllist = list(range(1805))
    j = 1
    # xpath1
    strfront = '/html/body/div[5]/table/tbody/tr['
    print("url == " + str(url))
    for i in range(1, 1805):
        try:
            htmllist[j] = html.xpath('/html/body/div[3]/table/tbody/tr[' + str(i) + ']/td[2]/span/a[1]/@href')[0]
            urlstr = str(url)
            htmlxpath = urlstr + htmllist[j]
            WriteToMySQL(htmlxpath)
            # print("htmlxpath == " + htmlxpath)
            # print("i == " + str(i) + " j == " + str(j) + " " + htmllist[j])
            j = j + 1

        except:
            pass
            # print("i == " + str(i) + " j == " + str(j))

        else:
            pass


def getpath3(url,html):

    htmllist = list(range(2005))
    j = 1
    # xpath1
    strfront = '/html/body/div[5]/table/tbody/tr['
    print("url == " + str(url))
    for i in range(1, 2005):
        try:
            htmllist[j] = html.xpath('/html/body/div[4]/table/tbody/tr[' + str(i) + ']/td[2]/span/a[1]/@href')[0]
            urlstr = str(url)
            htmlxpath = urlstr + htmllist[j]
            WriteToMySQL(htmlxpath)
            # print("htmlxpath == " + htmlxpath)
            # print("i == " + str(i) + " j == " + str(j) + " " + htmllist[j])
            j = j + 1

        except:
            pass
            # print("i == " + str(i) + " j == " + str(j))

        else:
            pass

def getpath4(url,html):

    htmllist = list(range(1805))
    j = 1
    # xpath1
    strfront = '/html/body/div[5]/table/tbody/tr['
    print("url == " + str(url))
    for i in range(1, 1805):
        try:
            htmllist[j] = html.xpath('/html/body/div[5]/table/tbody/tr[' + str(i) + ']/td[2]/span/a[1]/@href')[0]
            urlstr = str(url)
            htmlxpath = urlstr + htmllist[j]
            WriteToMySQL(htmlxpath)
            # print("htmlxpath == " + htmlxpath)
            # print("i == " + str(i) + " j == " + str(j) + " " + htmllist[j])
            j = j + 1

        except:
            pass
            # print("i == " + str(i) + " j == " + str(j))

        else:
            pass
def WriteToMySQL(htmlxpath):
    try:
        sql = "insert into htmlpath2017 (html) values " + "('" + htmlxpath + "')"
        print(sql)
        dbcursor.execute(sql)
        # writeevent.
        db.commit()
        # datanum + 1
        print("write finish " + ".")
    except:
        print("sql except")




def main():

    datanum = 0
    print("db")
    # url = f'https://spec.org/cpu2017/results/res2022q4/'
    url = f'https://spec.org/cpu2017/results/res2017q4/'
    gethtmlinfo(url)

main()