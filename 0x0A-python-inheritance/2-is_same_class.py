#!usr/bin/python3
def is_same_class(obj, a_class):
    """class checking function
    check if object is instance of a class

    Args:
        obj (_type_): the object to check
        a_class (_type_): the class to match with
    """
    
    if type(obj) == a_class:
        return True
    return False