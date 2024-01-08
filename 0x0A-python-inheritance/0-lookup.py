#!/usr/bin/python3
'''Module for lookup method.'''

def lookup(obj):
   """Returns a list of available attributes and methods of an object."""

   attributes = dir(obj)
   methods = []

   for attribute in attributes:
       if callable(getattr(obj, attribute)):
           methods.append(attribute)

   return methods

