#!/usr/bin/python3
"""
This script lists all cities from the database
"""

import MySQLdb as db
from sys import argv


if __name__ == '__main__':
    """
    Connects to database, gets states
    """
    if __name__ == "__main__":
        db_connect = db.connect(
                host="localhost",
                port=3306,
                user=argv[1],
                passwd=argv[2],
                db=argv[3]
                )

        db_cur = db_connect.cursor()

        db_cur.execute("SELECT cities.id, cities.name, \
                    states.name FROM cities JOIN states \
                        ON cities.state_id = states.id \
                            ORDER BY cities.id ASC")

        selected = db_cur.fetchall()
        for row in selected:
            print("{}".format(row))

        db_cur.close()
        db_connect.close()
