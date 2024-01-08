#!/usr/bin/python3
def no_c(my_string):
    final_result = ""
    for l in my_string:
        if l == "c" or l == "C":
            continue
        final_result += l
    return final_result
