#!/usr/bin/python3
import sys

"""

"""

class Square:
    """A class that defines a square by size, set the size of the square and
calculates the Area of the
    Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple) or (pos_1 < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        siz = self.size
        pos = self.__position[0]

        if siz == 0:
            print("\n")
        else:
            for i in range(siz):
                for j in range(siz):
                    if j < pos:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print("\n", end="")
