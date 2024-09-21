#!/usr/bin/python3
#script that lists all cities from the database hbtn_0e_4_usa


import sys
import MySQLdb
if __name__ == '__main__':
    conn = MuSQLdb.connect(user = sys.argv[1],
            password = sys.argv[2],
            db = sys.argv[3])
    cursor = conn.cursor()

    query = "SELECT cities.id, cities.name, states.name\
                    FROM cities LEFT JOIN states\
                    ON states.id = cities.state_id\
                    ORDER BY cities.id ASC"
    cursor.execute(query)
    row = cursor.fetchall()
    for r in row:
        print(r)

    cursor.close()
