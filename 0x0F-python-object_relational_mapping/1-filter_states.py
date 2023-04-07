#!/usr/bin/python3
"""
Script lists all states with name
starting with `N` from database `hbtn_0e_0_usa`
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv as av

    """
    Connects to the database
    """
    db_connect = MySQLdb.connect(
            host="localhost",
            user=av[1],
            port=3306,
            passwd=av[2],
            db=av[3])

    db_cur = db_connect.cursor()

    db_cur.execute("SELECT * FROM states WHERE name \
            LIKE BINARY 'N%' ORDER BY id ASC")

    """ fetch all at once """
    rows_selected = db_cur.fetchall()

    for row in rows_selected:
        print(f"{row}")
    db_cur.close()
    db_connect.close()
