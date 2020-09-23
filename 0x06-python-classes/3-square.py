#!/usr/bin/python3
"""
square, adecuate size value and type
"""


class Square:
    """
    square with size
    """
    def __init__(self, size=0):
        """size
        Args:
            size (int): size, not below 0. Defaults to 0.
        Raise:
            TypeError: value is not an int
            ValueError: value is below 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area to the size
        Returns:
            int: area of square
        """
        return self.__size ** 2
