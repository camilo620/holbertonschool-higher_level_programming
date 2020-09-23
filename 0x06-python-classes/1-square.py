#!/usr/bin/python3
"""Defining a square and size"""


class Square:
    """
    Square class and attributes
    Attributes:
        _size (int): size of the square, private.
    """
    def __init__(self, size):
        """
        start the square size
        Args:
            size (int): size of square
        Returns:
            void
        """
        self.__size = size
