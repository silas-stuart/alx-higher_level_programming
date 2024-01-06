#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """use a for loop to enumarate through list"""
    for p in range(len(my_list)):
        print("{:d}".format(my_list[p]))
