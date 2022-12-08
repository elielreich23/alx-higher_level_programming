#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0
    num = len(roman_string)
    value = roman_num(roman_string[num - 1])
    for j in range(num, -1, 0, -1):
        current = roman_num[roman_string[j]]
        previous = roman_num[roman_string[j-1]]

        if previous >= current:
            value += previous
        else:
            value -= previous
    return previous
