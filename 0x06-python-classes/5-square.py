#!/usr/bin/python3
import sys

"""

"""

class Square:
    """A class that defines a square by size, set the size of the square and
calculates the Area of the
    Square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        siz = self.size

        if siz == 0:
            print("\n")
        else:
            for i in range(siz):
                for j in range(siz):
                    print("#", end="")
                print("\n", end="")
