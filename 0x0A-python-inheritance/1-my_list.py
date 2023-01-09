#!/usr/bin/python3
"""
    This module inherits from list
"""


class Mylist(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
