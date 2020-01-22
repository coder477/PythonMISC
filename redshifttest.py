import psycopg2

import pymongo
import pprint
from datetime import datetime
import time
import json
import boto3
from bson.json_util import dumps

s3 = boto3.resource('s3')
client = pymongo.MongoClient("mongodb://mongouser:mongopassword@localhost/test") # defaults to port 27017

db = client['test']

# print the number of documents in a collection
print (db.cool_collection.count())
# 
# 
# # db.createUser({
# #     user: 'mongouser',
# #     pwd: 'mongopassword',
# #     roles: [{ role: 'readWrite', db:'test'}]
# # })
# 
# db.programming_data.remove({})
# result = db.programmingdata.create_index([('last_updated', pymongo.ASCENDING)],
#                                   unique=True)
sorted(list(db.programmingdata.index_information()))
 
 
# user_programming_data = [
#      {'user_id': 302, 'name': 'Luke',"test":"test"},
#   {'user_id': 401, 'name': 'Ziltoid'}]
# result = db.programming_data.insert_many(user_programming_data)
# print(result)
con = psycopg2.connect(dbname='codbrs', host='localhost', port='5439', user='rsuser', password='Redshift1973')
cur=con.cursor()
#    cur.execute("CREATE TYPE status AS ENUM ('true','false');")
#cur.execute("""create table if not exists kinesis_test;""")
# cur.execute("INSERT INTO test (id,num, data) VALUES (%s, %s, %s)",(100,100, "abc'def"))
query = "select * from co_programming_hub_data where last_updated >= '2018-09-20 00:00:00';"
cur.execute(query)
print ()
#db.programmingdata.remove({})
for each in cur.fetchall():
    cont=each[4]
    
    if(each[4] !=None and each[4]!="NA"):
        cont=json.loads(each[4].encode("utf-8")) 
    
#     elem={
#         'access_key':each[0],
#           'actor':json.loads(each[1].encode("utf-8")),
#           'verb':json.loads(each[2].encode("utf-8")),
#           'object':json.loads(each[3].encode("utf-8")),
#           'context':cont,
#           'result':(each[5]),
#           'last_updated':str(each[6])
#           } 
    elem={
                  'access_key':each[0],
        'actor':each[1],
        'verb':each[2],
        'object':each[3],
        'context':each[4],
        'result':(each[5]),
        'last_updated':str(each[6])
          }
#     elem=json.dumps(elem)
#     elem=json.loads(elem.replace("\'", '"'))
    elem1=json.dumps(elem)
    elem2=json.loads(elem1)
    #print type(elem1),elem1,elem2,type(elem2)
    result = db.programmingdata.insert(elem2,check_keys=False)
        
cur.close()
con.commit()
con.close()
i=0
for post in db.programmingdata.find():
    i=i+1 
    print post["last_updated"],i