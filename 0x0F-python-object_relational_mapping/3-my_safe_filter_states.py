#!/usr/bin/python3
"""write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!"""
import MySQLdb
import sys

conn = MySQLdb.connect(host= 'localhost',
        por= 3306,
        user= sys.argv[1],
        password= sys.argv[2],
        db= sys.argv[3])
cursor = conn.cursor()

cursor.execute("SELECT * FROM states WHERE BINARY name = ? ORDER BY states.id ASC", (sys.argv[4]))
row = cursor.fetchall()

for r in row:
    print(r)

cursor.close()
conn.close()
