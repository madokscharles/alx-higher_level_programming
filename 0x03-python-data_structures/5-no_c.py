#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for x in my_string:
        if x.lower() != "c":
            new += x
    return new
