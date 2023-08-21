#!usr/bin/python3
from sys import argv
import math


def factor(num):
    if num % 2 == 0:
        i = 2
        print("{}={}*{}".format(num, int(num//i), i))
    else:
        sq = int(math.sqrt(num)) + 1
        for i in range(3, sq, +2):
            if num % i == 0:
                print("{}={}*{}".format(num, int(num//i), i))
                return
            if num % (sq + 1) == 0:
                print("{}={}*{}".format(num, int(num//i), i))
                return
            if num % (sq - 1) == 0:
                print("{}={}*{}".format(num, int(num//i), i))
                return
            
def factors(filename):
    with open(filename, encoding="utf-8") as my_file:
        for i in my_file.readlines():
            n = int(i)
            result = factor(n)

if __name__ == "__main__":
    factors(argv[1])