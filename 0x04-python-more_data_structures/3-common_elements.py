#!/usr/bin/python3
def common_elements(set_1, set_2):
    res = {}
    for element in set_1:
        if element in set_2:
            res = element
    return res
