#!/usr/bin/python3
"""
Script defines a class State and an
instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

""" instance; used for defining mapped classes """
Base = declarative_base()


class State(Base):
    """
    defines class State which inherits from Base
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
