#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for count in my_list:
        num += count[0] * count[1]
        den += count
        return (num / den)
