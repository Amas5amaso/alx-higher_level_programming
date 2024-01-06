#!/usr/bin/python3


class LockedClass:
    def __init__(self):
        self.__dict__['first_name'] = None

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("can't set attribute")
        else:
            self.__dict__[name] = value

# testing

lc = LockedClass()


lc.first_name = 'John'
print(lc.first_name)

try:
    lc.last_name = 'Doe'
except AttributeError as e:
    print(e)
