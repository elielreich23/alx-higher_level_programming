#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        sort_keys = sorted(a_dictionary.keys())
        for j in sort_keys:
            print("{:s}: {}".format(j, a_dictionary(j)))
