#!/usr/bin/python3
"""Defines a locked class."""


class Lockclass:
    """
    Prevent the user from instantiating new lockclass attributes
    for anything but attribute called 'first_name'.
    """

    _ _slots_ _ = ["first_name"]
