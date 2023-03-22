#!/usr/bin/python3
"""
Script prints the State objects with the name
passed as argument from the database `hbtn_0e_6_usa`
"""

from sys import argv as av
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
    Accesses the database and connects to database
    """
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.
                format(av[1], av[2], av[3]),
                pool_pre_ping=True)

    """ create a session """
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == av[4]).all()
    if result:
        for row in result:
            if row.name == av[4]:
                print("{}".format(row.id))
    else:
        print("Not found")
    session.close()
