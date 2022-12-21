#!/usr/bin/python3
"""Square module definition.
This module defines a simple `Square` class
"""


class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self._Square__size ** 2

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def my_print(self):
        """Prints a ``Square`` filled with '#'"""
        if self.size:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
