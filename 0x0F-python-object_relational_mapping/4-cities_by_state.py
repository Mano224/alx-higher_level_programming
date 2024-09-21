#!/usr/bin/python3
#script that lists all cities from the database hbtn_0e_4_usa


import sys
import MySQLdb

conn = MuSQLdb.connect(user = sys.argv[1],
        password = sys.argv[2],
        db = sys.argv[3])
cursor = conn.cursor()

query = "SELECT * FROM cities ORDER BY cities.id ASC"
cursor.execute(query)
row = cursor.fetchall()
for r in row:
    print(r)

cursor.close()


