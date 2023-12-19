#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """prints an integer with "{:d}".format()

    if a valueError message is caught, a corresponding
    message is printed to standard error

    Args:
    value (int): The integer to print

    Returns:
    if a TypeError or Value occurs - False
    otherwise - True
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as exc:
        print("Exception: ", exc, file=sys.stderr)
        return False
