#!/usr/bin/python3
"""
This script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connects to the database, gets states
    """
    if __name__ == "__main__":
        db_connect = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )

        db_cur = db_connect.cursor()

        db_cur.execute("SELECT * FROM states WHERE name \
                LIKE BINARY 'N%' ORDER BY id")

        selected = db_cur.fetchall()
        for row in selected :
            print("({}, \'{}\')".format(row[0], row[1]))

        db_cur.close()
        db_connect.close()
