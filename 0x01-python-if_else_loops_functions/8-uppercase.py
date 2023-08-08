#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 97 <= ord(char) <= 122:
            print(chr(ord(char) - 32), end='')
        else:
            print(char, end='')
    print()
