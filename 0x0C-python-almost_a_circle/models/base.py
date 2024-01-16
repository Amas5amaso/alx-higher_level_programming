#!/usr/bin/python3
"""Module for Base class"""


class Base:
    """Presentation of base oop hierarchy."""

    __nb_objects = 0

    def __init__(self, id=NONE):
        """constructor."""
        if id is not NONE:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
