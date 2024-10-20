'''
Tracy Ye
JST
SoftDev
skeleton/stub :: SQLITE3 BASICS : adventuring into SQLite3
2024-10-18
Time Spent :
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

dict = []
with open("courses.csv", newline='') as file:
    r = csv.DictReader(file)
    for i in r:
        dict.append(i)
# print(dict)
        
c.execute("CREATE TABLE cour (code TEXT,mark INTEGER,id INTEGER)")
for row in dict:
    vals = "("
    vals += '"' + (row.get("code")) + '", '
    vals += (row.get("mark")) + ", "
    vals += (row.get("id")) + ")"
    
    #print(vals)
    c.execute(f'INSERT INTO cour (code,mark,id) VALUES {vals}')

#==========================================================
    
dict = []
with open("students.csv", newline='') as file:
    r = csv.DictReader(file)
    for i in r:
        dict.append(i)
#print(dict)
        
c.execute("CREATE TABLE studs (name TEXT,age INTEGER,id INTEGER)")
for row in dict:
    vals = "("
    vals += '"' + (row.get("name")) + '", '
    vals += (row.get("age")) + ", "
    vals += (row.get("id")) + ")"
    
    #print(vals)
    c.execute(f'INSERT INTO studs (name,age,id) VALUES {vals}')
    
#==========================================================

db.commit() #save changes
db.close()  #close database













