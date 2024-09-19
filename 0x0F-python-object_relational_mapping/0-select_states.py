#!/usr/bin/python3
#script that lists all states from the database hbtn_0e_0_usa
import MySQLdb
import sys

conn = MySQLdb.connect(host = "localhost",
        user = sys.argv[1], password = sys.argv[3], port = 3306, db = sys.argv[3], charset="utf8")

cursur = conn.cursor()
cursur.execute("SELECT * FROM states")
r = cursur.fetchall()
for row in r:
    print(row)
cursur.closs()

