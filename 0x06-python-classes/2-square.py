#!/usr/bin/python3
# 2-square.py by Madoks Charles


class Square:
    """A class that represents a Square"""

    def __init__(self, size=0):
        """Initializing square class
        Args:
            size: represents size of square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
