#!/usr/bin/python3
"""
Script defines a class City and inherits from
Base (imported from model_state)
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

""" instance; used for defining mapped classes """
Base = declarative_base()


class City(Base):
    """
    defines class City which inherits from Base
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
