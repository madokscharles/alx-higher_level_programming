#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Prevents user from creating new instance, except first_name
    """

     __slots__ = ["first_name"]
