#! /Users/vhaefeli/.brew/bin python3.11

def all_thing_is_obj(object: any) -> int:
    typeobj = type(object)
    print(typeobj)
    
    match typeobj:
        case list():
            print("List : <classe 'list'>")
        case tuple():
            print("Tuple : <classe 'tuple'>")
    return 42