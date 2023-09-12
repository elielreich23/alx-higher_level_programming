#!usr/bin/python
BaseGeometry = __import__('7-base_geometry').BaseGeomety

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
        