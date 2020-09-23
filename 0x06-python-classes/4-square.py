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
            size (int): size, not below 0.
            Defaults to 0.
        Raises:
            TypeError: is not an int
            ValueError: is below 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area of the size
        Returns:
            int: area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter for size
        Returns:
            int: Size of the square
        """
        return self.__size

    @size.setter
    def size(self, siz):
        """setter for size
        Args:
            siz (int): New size of square, 0 or above
        Raises:
            TypeError: is not an integer
            ValueError: is below 0
        """
        if type(siz) is not int:
            raise TypeError("size must be an integer")
        elif siz < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = siz

    def my_print(self):
        """Prints a square
        """
        r = range(self.__size)
        if self.__size == 0:
            print()
        else:
            print("\n".join(["".join(["#" for i in r]) for y in r]))
