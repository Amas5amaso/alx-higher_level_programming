#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """Represents a rectangle with protected attributes."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner. Defaults to 0.
            id (str, optional): The unique identifier of the rectangle. Defaults to None.
        """

        super().__init__(id)  # Call the constructor of the base class
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle, ensuring it's positive."""
        if value > 0:
            self.__width = value
        else:
            raise ValueError("Width must be positive.")

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle, ensuring it's positive."""
        if value > 0:
            self.__height = value
        else:
            raise ValueError("Height must be positive.")

    @property
    def x(self):
        """Returns the x-coordinate of the top-left corner."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the top-left corner."""
        self.__x = value

    @property
    def y(self):
        """Returns the y-coordinate of the top-left corner."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the top-left corner."""
        self.__y = value

