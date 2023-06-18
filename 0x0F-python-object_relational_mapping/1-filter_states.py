#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                            passwd=argv[2], db=argv[3])

    c = conn.cursor()
    c.execute('SELECT * FROM persons WHERE LastName LIKE "N%"')
    rows = c.fetchall()

    for row in rows:
        print(row)
