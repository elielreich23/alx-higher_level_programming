#!/usr/bin/python3
def element_at(my_list, element, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        my_list[idx] = element
        return my_list
