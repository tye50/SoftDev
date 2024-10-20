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

command = "create table courses(code text, mark integer, id integer)"
c.execute(command)

dict = []

with open("course.csv", newline='') as file:
    r = csv.DictReader(file)
    for i in r:
        dict.append(i)
print(dict)
for row in dict:
    vals = "("
    vals = vals + (row.get("code")) + ", "
    vals = vals + (row.get("mark")) + ", "
    vals = vals + (row.get("id")) + ")"
    
    print(vals)
    command = f'insert into courses (code,mark,id) values {vals}'
    print(command)
    c.execute(command)
#==========================================================

db.commit() #save changes
db.close()  #close database













