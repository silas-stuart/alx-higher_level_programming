#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        """if success then use node idx of list to
            be element and return udpated list
        """
        my_list[idx] = element
        return my_list
