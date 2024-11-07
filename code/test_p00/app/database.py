import sqlite3
import csv

    # create main tables
db = sqlite3.connect("data.db")
c = db.cursor()
if (c.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='accounts'").fetchall() == []):
    c.execute("CREATE TABLE accounts(username TEXT, password TEXT)")
    c.execute("CREATE TABLE blogs(owner TEXT, title TEXT, entry_1 TEXT)")
db.commit()
db.close()

def addAcc(uname, pw):
    db = sqlite3.connect("data.db")
    c = db.cursor()
    c.execute(f"INSERT INTO accounts VALUES ('{ uname }', '{ pw }')")
    db.commit()
    db.close()
