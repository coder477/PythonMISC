'''
Created on 17-May-2016

@author: snehapaturu
'''

import pymysql
import sys
import csv
import xlwt
from tempfile import TemporaryFile
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')
 
db = pymysql.connect(host="localhost",  # your host, usually localhost
                     user="vocabprep_adm",  # your username
                     passwd="vocab_Prep",  # your password
                     db="django_vocab_prep")  # name of the data base
  
cur = db.cursor() 
cs = csv.writer(open("temp.csv","wb"))
qry1="""select a.id,a.meaning_id,b.meaning,b.spelling_id,c.spelling,a.spelling_id,d.spelling,a.part_of_speech 
from meanings_forms_mapping a,meanings b, spellings c, spellings d
 where a.meaning_id=b.meaning_id and a.spelling_id=d.spelling_id and b.spelling_id=c.spelling_id 
""";
cur.execute(qry1)
a=[]
b=[]
c=[]
d=[]
eg=[]
f=[]
g=[]
h=[]
for each in cur.fetchall():
    
    a.append(each[0])
    b.append(each[1])
    c.append(each[2])
    d.append(each[3])
    eg.append(each[4])
    f.append(each[5])
    g.append(each[6])
    h.append(each[7])
 
 
for i,e in enumerate(a):
    sheet1.write(i,0,unicode(e)) 

for i,e in enumerate(b):
    sheet1.write(i,1,unicode(e))
    
for i,e in enumerate(c):
    e = e.decode('utf-8')
    sheet1.write(i,2,unicode(e))   

for i,e in enumerate(d):
    sheet1.write(i,3,unicode(e)) 
    
for i,e in enumerate(eg):
    e = e.decode('utf-8')
    sheet1.write(i,4,unicode(e)) 
    
for i,e in enumerate(f):
    sheet1.write(i,5,unicode(e)) 
    
for i,e in enumerate(g):
    e = e.decode('utf-8')
    sheet1.write(i,6,unicode(e)) 
    
for i,e in enumerate(h):
    
    sheet1.write(i,7,unicode(e)) 
# rows = zip(a,b,c,d,e,f,g,h)
# for row in rows:
#     xsheet.write(row)
name = "random.xls"
book.save(name)
book.save(TemporaryFile())

