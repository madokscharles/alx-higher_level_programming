#!/usr/bin/python3
""" This module contains a class to serve as base for other classes """


import json
import turtle


class Base:
    """ Represents base of all classes created """

    __nb_objects = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation to file """
        LO_dict = []
        if list_objs is not None:
            LO_dict = [x.to_dictionary() for x in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(LO_dict))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance of the class and return it """
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        elif cls.__name__ == "Square":
            inst = cls(1)
        else:
            return None
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                contentRead = f.read()
        except:
            return []
        listOfDicts = cls.from_json_string(contentRead)
        return [cls.create(**inst) for inst in listOfDicts]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw list of rec ands squares """
        for rec in list_rectangles:
            rec = rec.to_dictionary()
            turtle.up()
            turtle.setx(rec["x"])
            turtle.sety(rec["y"])
            turtle.down()
            turtle.fd(rec["width"])
            turtle.right(90)
            turtle.fd(rec["height"])
            turtle.right(90)
            turtle.fd(rec["width"])
            turtle.right(90)
            turtle.fd(rec["height"])

        for square in list_squares:
            size = square["size"]
            turtle.up()
            turtle.setx(square["x"])
            turtle.sety(square["y"])
            turtle.down()
            turtle.fd(size)
            turtle.right(90)
            turtle.fd(size)
            turtle.right(90)
            turtle.fd(size)
            turtle.right(90)
            turtle.fd(size)
            turtle.right(90)
