#!/usr/bin/python3
""" Module contains a rectangle class """

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes fields of the object """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
