#!/usr/bin/python3

"""Class to define Rectangle"""
class Rectangle:
    """porps of the rectangle"""

    def __init__(self, width=0, height=0):
        """initialize the rectangle
        Args:
            width: the width of the rectangle
            height: the height
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self.width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("the width must be an integer")
        if value < 0:
            raise TypeError("width must be >=0")
        self.width = value
    
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("the height must be an integer")
        if value < 0:
            raise TypeError("height must be >=0")
        self.height = value

    def area(self):
        """returns area"""
        return (self.__width * self.__height)
    
    def perimeter(self):
        """returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))