#! /usr/bin/env python3

def NULL_not_found(object: any) -> int:
    typeobj = type(object)
    typeobjstr = str(typeobj)
    match (typeobjstr, object):
        case ("<class 'NoneType'>", None):
            print("Nothing : None : <class 'NoneType'>")
        case ("<class 'float'>", nan):
            print("Cheese : nan <class 'float'>")
        case ("<class 'int'>", 0):
            print("Zero : 0 <class 'int'>")
        case ("<class 'str'>", ''):
            print("Empty : <class 'str'>")
        case ("<class 'bool'>", False):
            print("Fake : False <class 'bool'>")
        case _:
          print("Type not found")
          return 1
    return 0