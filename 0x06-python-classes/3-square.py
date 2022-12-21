#!/usr/bin/python3
"""
class that defines a square
"""

class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        """Computes the area of the ``Square``.
        Returns:The area of the ``Square``.
        """
        return self._Square__size ** 2
