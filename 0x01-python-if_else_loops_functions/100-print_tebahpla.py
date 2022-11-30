#!/usr/bin/python3
c = 0
for m in range(122, 96, -1):
    if m % 2 == 0:
        c = m
    else:
        c = m - 32
    print('{}'.format(chr(c)), end='')
