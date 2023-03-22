#!/usr/bin/python3
"""
Script takes in the name of a state as an argument
and lists all cities of that state
using the database `hbtn_0e_0_usa'
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv as av

    """
    Accesses the database and connects to database
    """
    db_connect = MySQLdb.connect(
            host="localhost",
            user=av[1],
            port=3306,
            passwd=av[2],
            db=av[3])

    db_cur = db_connect.cursor()

    db_cur.execute(
                "SELECT * FROM cities JOIN states ON \
                        cities.state_id = states.id WHERE \
                        states.name = %s ORDER BY \
                        cities.id ASC", (av[4],))

    """ fetch all at once """
    rows_selected = db_cur.fetchall()

    print(", ".join([row[2] for row in rows_selected]))
    db_cur.close()
    db_connect.close()
