from pycorenlp import StanfordCoreNLP
import pymysql

db = pymysql.connect(host="localhost",user="root",password="Torres@09",db="ArticleNYT")
print(db)
nlp = StanfordCoreNLP('http://localhost:9000')
print(nlp)
cur = db.cursor()
cur.execute("""SELECT COUNT(NID) FROM Tech_2018;""")
temp = cur.fetchone()
counter = temp[0] - 1
print(counter)
while(counter>=0):
    try:
        cur.execute("""SELECT Abstract from Tech_2018 WHERE NID = %s;""",(counter))
        tmpabs = cur.fetchone()
        finabs = str(tmpabs[0])
        res = nlp.annotate(finabs,
                    properties={
                        'annotators': 'sentiment',
                        'outputFormat': 'json',
                        'timeout': 1000000000,
                        "ssplit.eolonly": "true"
                    })
        for s in res["sentences"]:
            print("%s" %(s["sentimentValue"]))
        score = s['sentimentValue']
        try:
            cur.execute("""UPDATE Tech_2018 SET Score = %s WHERE NID = %s;""",(score,counter))
            db.commit()
            print("Score inserted")
            counter-=1
        except:
            db.rollback()
            print("Score insertion failed")
    except:
        db.rollback()
        print("Fail")
db.close()