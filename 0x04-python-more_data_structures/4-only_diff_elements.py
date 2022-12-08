#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_element = set()
    for x in set_1:
        if x not in set_2:
            diff_element.add(x)
    for y in set_2:
        if y not in set_1:
            diff_element.add(y)
    return diff_element
