import sqlite3
import csv

    # create main tables
db = sqlite3.connect("data.db")
c = db.cursor()
if (c.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='accounts'").fetchall() == []):
    c.execute("CREATE TABLE accounts(username TEXT NOT NULL, password TEXT NOT NULL)")
    c.execute("CREATE TABLE blogs(owner TEXT NOT NULL, title TEXT NOT NULL, entry_1 TEXT NOT NULL)")
db.commit()
db.close()

def addAcc(uname, pw):
    db = sqlite3.connect("data.db")
    c = db.cursor()
    c.execute(f"INSERT INTO accounts VALUES ('{ uname }', '{ pw }')")
    db.commit()
    db.close()

def newBlog(uname, title, firstEntry):
    db = sqlite3.connect("data.db")
    c = db.cursor()
    c.execute(f"CREATE TABLE { uname }---{ title }(entryID INTEGER, entry TEXT)")
    c.execute(f"INSERT INTO blogs