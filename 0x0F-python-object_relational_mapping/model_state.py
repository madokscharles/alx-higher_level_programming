#!/usr/bin/python3
"""
This script defines a State class and a
Base class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class State(Base):
    """
    Defines a State class which inherits from the Base class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)