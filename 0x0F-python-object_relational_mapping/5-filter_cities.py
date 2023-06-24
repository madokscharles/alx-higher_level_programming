#!/usr/bin/python3
"""
This script takes in the name of state as
an argument and lists all its cities
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
        db_cur.execute(
                """SELECT cities.name FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name=%s
                ORDER BY 'cities.id' ASC;""", (argv[4],))

        selected = db_cur.fetchall()
        print(", ".join(row[0] for row in selected))

        db_cur.close()
        db_connect.close()
