#!/usr/bin/python3

"""lists all states from 
the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':

    """
    Access to the database and get the states
    from the database.
    """
    conn = MySQLdb.connect(host="localhost", port="3306", 
            user=sys.argv[1], 
            passwd=sys.argv[2], db=sys.argv[3])
    c = conn.cursor()
    c.execute('SELECT * FROM persons ORDER BY id')
    rows = c.fetchall()
    for row in rows:
        print(row)

