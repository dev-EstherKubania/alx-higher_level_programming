#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    for  names dir(hidden_4):
        if names[:2] != "__":
            print("{:s}".format(names))
