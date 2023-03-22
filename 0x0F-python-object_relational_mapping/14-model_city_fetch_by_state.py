#!/usr/bin/python3
"""
Script prints all City objects
from database `hbtn_0e_6_usa`
"""

from sys import argv as av
from model_state import State, Base
from model_city import City
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

    result = session.query(
                State, City).filter(
                        State.id == City.state_id).order_by(City.id).all()
    for state, city in result:
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))

    session.close()
