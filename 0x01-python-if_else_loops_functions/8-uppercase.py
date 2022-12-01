#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) in range(97, 123):
            y = ord(x) - 32
        else:
            y = ord(x)
        print("{:c}".format(y), end='')
    print("")
