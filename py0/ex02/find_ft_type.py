#! /usr/bin/env python3

def all_thing_is_obj(object: any) -> int:
    typeobj = type(object)
    typeobjstr = str(typeobj)
    match (typeobjstr):
        case ("<class 'list'>"):
            print("List : <class 'list'>")
        case ("<class 'tuple'>"):
            print("Tuple : <class 'tuple'>")
        case ("<class 'set'>"):
            print("Set : <class 'set'>")
        case ("<class 'dict'>"):
            print("Set : <class 'dict'>")
        case ("<class 'str'>"):
            print("Brian is in the kitchen : <class 'str'>")
        case _:
          print("Type not found")
    return 42