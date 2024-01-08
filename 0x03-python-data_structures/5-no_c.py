#!/usr/bin/python3
def no_c(my_string):
    """for every letter in string check for c"""
    result = ""
    for l in my_string:
        if l == "c" or l == "C":
            continue
        result += l
    return result
