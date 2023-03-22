#!/usr/bin/python3
"""
Script delets all State objects with a name
containing the letter a from database `hbtn_0e_6_usa`
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

    result = session.query(State).all()
    for row in result:
        if 'a' in str(row.name):
            session.delete(row)
    session.commit()
    session.close()
