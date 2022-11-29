#!/usr/bin/python3
def uppercase(str):
    """Print a string in upperrcase."""
    for c in str:
        if ord(c) >= 65 and ord(c) <= 90:
            print("{}".format(c), end="")
