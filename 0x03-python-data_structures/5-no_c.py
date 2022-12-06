#!/usr/bin/python3
def no_c(my_string):
    new_list = my_string
    string = ''
    for char in new_list:
        if char !='c' and char != 'C':
            string += char
    return string
