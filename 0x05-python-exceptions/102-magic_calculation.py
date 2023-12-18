#!/usr/bin/python3
def magic_calculation(a, b):
    """This function performs a calculation given by args"""
    a: The first operand
    b: The second operand
    return:
    """A value based on the specified operation"""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += pow(a, b) / i
        except Exception:
            result = b + a
            break
