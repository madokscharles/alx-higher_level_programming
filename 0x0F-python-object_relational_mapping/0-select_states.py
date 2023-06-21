#!/usr/bin/python3
"""
Script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connects to database
    """
    db_connect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    db_cur = db_connect.cursor()

    db_cur.execute("SELECT * FROM states ORDER BY id")

    selected = db_cur.fetchall()

    for row in selected:
        print("({}, \'{}\')".format(row[0], row[1]))

    db_cur.close()
    db_connect.close()
