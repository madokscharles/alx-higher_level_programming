#!/usr/bin/python3
"""
Script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Get states from database
    """
    db_connect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    selected = db_cursor.fetchall()

    for row in selected :
        print("({}, \'{}\')".format(row[0], row[1]))

    db_cursor.close()
    db_connect.close()
