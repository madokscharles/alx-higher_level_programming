#!/usr/bin/python3
"""
Script adds the State object "Louisiana"
to the database `hbtn_0e_6_usa`
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
    session.close()