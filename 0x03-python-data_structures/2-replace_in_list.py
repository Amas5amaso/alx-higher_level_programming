#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        my_list = list(my_list)
        my_list._setitem_(idx, element)
        return my_list
