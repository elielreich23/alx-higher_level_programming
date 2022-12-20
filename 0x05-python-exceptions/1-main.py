#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
been_print = safe_print_integer(value)
if not been_print:
    print("{} is not an integer".format(value))

value = -89
been_print = safe_print_integer(value)
if not been_print:
    print("{} is not an integer".format(value))

value = "School"
been_print = safe_print_integer(value)
if not been_print:
    print("{} is not an integer".format(value))