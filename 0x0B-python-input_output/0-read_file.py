#!/usr/bin/python3


def read_file(filename=""):
   """Reads a text file (UTF8) and prints its contents to stdout.

   Args:
       filename (str, optional): The name of the file to read. Defaults to "".
   """

   with open(filename, "r", encoding="utf-8") as file:
       contents = file.read()
       print(contents)


