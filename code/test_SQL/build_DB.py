import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

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

# ---

c.execute("""IF COL_LENGTH('cour', 'sound')IS NOT NULL
    ALTER TABLE cour ADD sound TEXT""")
#==========================================================

db.commit() #save changes
db.close()  #close database












