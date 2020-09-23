#!/usr/bin/python3
"""
square
"""


class Square:
    """
    Square with size
    """
    def __init__(self, size=0, position=(0, 0)):
        """square
        Args:
            size (int): Size
            position (tuple): square position.
        """
        self.size = size
        self.position = position

    def area(self):
        """area of the size
        Returns:
            int: area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter for size
        Returns:
            int: Size
        """
        return self.__size

    @size.setter
    def size(self, siz):
        """setter for size
        Args:
            siz (int): New size of square 0 or above
        Raises:
            TypeError: not an integer
            ValueError: below 0
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

        p = range(self.__position[0])
        
        if self.__size == 0:
            print()
        else:
            if self.position == (0, 0):
                print("\n".join(["".join(["#" for i in r]) for y in r]))
            else:
                for _ in range(self.__position[1]):
                    print()
                for _ in r:
                    print("".join([" " for s in p]), end="")

                    print("".join(["#" for i in r]))

    @property
    def position(self):
        """Getter of position
        Returns:
            position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter
        Args:
            value: the position
        Raises:
            TypeError: tuple dont have adecuate values
        """
        if type(value) is not tuple or len(value) is not 2 or\
            type(value[0]) is not int or value[0] < 0 or\
                type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
