#!/usr/bin/python3
"""
    This module returns the lists of available attributes
    and methods of an object.
"""


def lookup(obj):
    """ This function looks out for attributes and methods of an obj """
    return dir(obj)
