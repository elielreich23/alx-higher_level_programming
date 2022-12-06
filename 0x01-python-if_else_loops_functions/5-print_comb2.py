#!/usr/bin/python3
# program to print number form 1 -100 with in format 00 followed by a comma
for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=", ")
