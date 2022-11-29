#!/usr/bin/python3
def isuppercase(letter):
    if ord(letter) >= 97 and ord(letter) <= 122:
        return (ord(letter) - 32)
    else:
        return (ord(letter))


def uppercase(str):
    new = ""
    for letter in str:
        new += "%c" % isuppercase(letter)
    print("{:s}".format(new))
