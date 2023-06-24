#!/usr/bin/python3
"""
This script lists all State objects that contain
the letter a from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    Connects to database
    """
    if __name__ == "__main__":
        db_engine = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3])

        engine = create_engine(db_engine)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter(State.name.contains('a'))

        if state is not None:
            for s in state:
                print('{0}: {1}'.format(s.id, s.name))
