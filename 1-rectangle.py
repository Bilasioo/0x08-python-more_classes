#!/usr/bin/python3

#Defining rectangle class
class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initialize new rectangle
        Args:
            width (int): The rectangle width
            height (int): The rectangle height

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        #seting rectangle width
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        #setting rectangle height
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
