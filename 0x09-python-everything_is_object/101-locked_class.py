#!/usr/bin/python3
"""This defines a locked class"""


class LockedClass:
    """
    Allows only new instance attribute called first_name
    """

    __slots__ = ["first_name"]
