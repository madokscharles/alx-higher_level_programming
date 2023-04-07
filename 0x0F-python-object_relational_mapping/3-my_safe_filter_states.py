#!/usr/bin/python3
"""
Script takes in an argument and displays
all the values in the states table of `hbtn_0e_0_usa`
where name matches the argument
but this time, one safe from MySQL injections!
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

    db_cur.execute("SELECT * FROM states WHERE name = %s \
            ORDER BY id ASC", (av[4],))

    """ fetch all at once """
    rows_selected = db_cur.fetchall()

    for row in rows_selected:
        print(f"{row}")
    db_cur.close()
    db_connect.close()
