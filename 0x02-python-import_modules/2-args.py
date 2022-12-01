#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arglen = len(argv)

    if arglen > 1:
        index = 0
        if arglen > 2:
            print("{:d} arguments:".format(arglen - 1))
        else:
            print("{:d} argument:".format(arglen - 1))
        for x in argv:
            index += 1
            if index != 1:
                print("{:d}: {}".format(index - 1, x))
    else:
        print("0 arguments.")
