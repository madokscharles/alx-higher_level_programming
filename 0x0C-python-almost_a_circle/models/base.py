#!/usr/bin/python3
""" Module contains a class to serve as base for other classes """

import csv
import json
import os
import turtle


class Base:
    """ Represents base of all classes created """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
