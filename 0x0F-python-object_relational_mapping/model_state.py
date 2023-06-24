#!/usr/bin/python3
"""
This script defines a State class and a
Base class
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Defines a State class which inherits from the Base class

    Attribute:
        __tablename__ (str): Table name of the class
        id (int): State id
        name (str): State name
    """
    __tablename__ = 'states'

    id = Column(Integer,
                unique=True,
                primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
