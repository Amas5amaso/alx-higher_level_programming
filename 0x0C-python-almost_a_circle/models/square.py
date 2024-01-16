#!/usr/bin/python3

class Square:
   def __init__(self, side, x=0, y=0, id=None):
       self._validate_integer("side", side)
       self._validate_positive("side", side)
       self._side = side

       self._validate_integer("x", x)
       self._validate_non_negative("x", x)
       self._x = x

       self._validate_integer("y", y)
       self._validate_non_negative("y", y)
       self._y = y

       self.id = id


   def to_dictionary(self):
       """
       Returns a dictionary representation of the Square object.

       Returns:
           dict: A dictionary containing the id, size, x, and y coordinates of the Square.
       """
       return
           "id": self.id,
           "size": self.side,
           "x": self.x,
           "y": self.y,

