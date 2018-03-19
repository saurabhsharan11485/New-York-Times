import matplotlib
import numpy
import math
import pymysql
import re
import matplotlib.pyplot as plt
def nytgraph():
    db = pymysql.connect(host="localhost",user="root",password="Torres@09",db="ArticleNYT")
    print(matplotlib.__version__)
    cur = db.cursor()
    cur.execute("SELECT TableName FROM SentimentScore WHERE TableName like 'News%';")
    temptn = cur.fetchall()
    tnlist = []
    for i in temptn:
        s = str(i)
        s = re.sub("[^0-9]",'',s) 
        tnlist.append(s)
    print(tnlist)
    sclist = []
    for i in tnlist:
        cur.execute("SELECT SentimentScore FROM SentimentScore WHERE TableName like '%{}%'".format(i))
        tempsc = cur.fetchone()
        s = tempsc[0]
        score = float(s)
        sclist.append(score)
    print(sclist)
    plt.plot(tnlist,sclist,"rx--")
    plt.legend("Year","Sentiment Score")
    plt.xscale("linear")
    plt.show()
    db.close()