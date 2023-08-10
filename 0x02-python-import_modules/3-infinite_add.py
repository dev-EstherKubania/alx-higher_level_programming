#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    thesum = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            thesum += int(arg)
    print(thesum)
