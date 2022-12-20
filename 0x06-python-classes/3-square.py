#!/usr/bin/python3
# 3-square.py by Madoks Charles
"""A module that defines a square """


class Square:
    """A class that represents a square"""

     def __init__(self, size=0):
         """Initializing square class
         Args:
             size: represnets the size of the square defined
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

      def area(self):
          """
          Calculate area of the square
          Returns: The square of the size
          """

          return self.__size ** 2
