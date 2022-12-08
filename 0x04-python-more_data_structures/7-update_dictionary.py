#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        new = a_dictionary
        new[key] = value
        return new