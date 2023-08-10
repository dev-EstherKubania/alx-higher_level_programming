#!/usr/bin/python3

import sys

if __name__ == "__main__":
    l = len(sys.argv)

    if l == 1:
        print("{:d} arguments.".format(l - 1))
    elif l == 2:
        print("{:d} argument:".format(l - 1))
    else:
        print("{:d} arguments:".format(l - 1))
    for i in range(1, l):
        print("{:d}: {:s}".format(i, sys.argv[i]))
