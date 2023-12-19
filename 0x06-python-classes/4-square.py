#!/usr/bin/python3
"""square module."""

class square:
    """Define a square."""

    def __init__(self, size=0):
        """constructor.

        Args:
            size: Length of a side of the square.
        """
        self.size = size
        @property
        def size(self):
            """property for the length of a side of this square.

            Raises:
                TypeError: if size is not an integer.
                ValuEroor: if size is less than 0.
            """
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError('size must be an integer')
            if value < 0:
                raise ValueError('size must be an >= 0')
            self.__size = value

        def area(self):
            """Area ot this square.

            Returns:
                The size squared.
            """
            return self.__size ** 2
