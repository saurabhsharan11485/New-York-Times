import requests
import json
import string
import time
import pymysql
from pycorenlp import StanfordCoreNLP

db = pymysql.connect(host="localhost",user="root",password="Torres@09",db="ArticleNYT")
print(db)
nlp = StanfordCoreNLP('http://localhost:9000')
counter = 0
cur = db.cursor()
try:
    cur.execute("""ALTER TABLE `Tech_2018` CHANGE `NID` `NID` INT(250) NOT NULL;""")
    db.commit()
    print("Type change 1")
except:
    db.rollback()

cur.execute("""SELECT NID FROM Tech_2018 ORDER BY NID DESC LIMIT 1;""")
temp = cur.fetchone()
print(temp)
#counter = temp[0] + 1
if(temp == None):
    counter = 0
else:
    counter = temp[0] + 1
print(counter)
try:
    cur.execute("""ALTER TABLE `Tech_2018` CHANGE `NID` `NID` VARCHAR(250) NOT NULL;""")
    db.commit()
    print("Type change 2")
except:
    db.rollback()

try:
    for i in range(0,1000):
        url="https://api.nytimes.com/svc/search/v2/articlesearch.json"
        parameters = {
            'api-key' : "f06354ed420c4174bf083f6b52107420",
            'q' : 'technology',
            'begin_date': "2017-10-02",
            'end_date' : "2018-03-14",
            'page' : i,
            'fl' : 'snippet,pub_date',
            'sort' : "oldest"
        }
        r = requests.get(url,params=parameters)
        print(r.status_code)
        articledata_dict = json.loads(r.text)
        newsblocks = articledata_dict['response']['docs']
        db_conn = db.cursor()
        for e in newsblocks:
                print(e['snippet'])
                print(e['pub_date'])
                print(e['score'])
                try:
                    db_conn.execute("""INSERT INTO Tech_2018 VALUES (%s,%s,%s,%s);""",(str(counter),e['snippet'],e['pub_date'],e['score']))
                    db.commit()
                    counter+=1
                    print("Success")
                except Exception:
                    db.rollback()
                    print("Fuck ")
        time.sleep(2)
except:
    print()
cur.execute("""ALTER TABLE `Tech_2018` CHANGE `NID` `NID` INT(250) NOT NULL;""")
db.commit()
print("Type change 3")
db.close()