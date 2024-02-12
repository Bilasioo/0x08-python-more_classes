#!/usr/bin/python3

class Rectangle:
    """
        number_of_instances (int): The rectangle instances number
        print_symbol (any): The string representation symbol
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            width (int): The new rectangle width
            height (int):the new rectangle height
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
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
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns rectangle with the greater area
        Args:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The last  rectangle

        Raise:
            TypeError: If either of rect_1 or rect_2 is not a rectangl
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
            Returns new  width and height equal to size of the rectangle

            size (int): The new Rectangle width and height.
        """
        return (cls(size, size))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        r = []
        for k in range(self.__height):
            [r.append(str(self.print_symbol)) for j in range(self.__width)]
            if k != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
