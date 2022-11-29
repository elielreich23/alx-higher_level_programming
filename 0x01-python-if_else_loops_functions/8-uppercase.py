#!/usr/bin/python3
def isuppercase(l):
    if ord(l) >= 97 and ord(l) <= 122:
        return (ord(l) - 32)
    else:
        return (ord(l))


def uppercase(str):
    new = ""
    for l in str:
        new += "%c" % isuppercase(l)
    print("{:s}".format(new))
