#!/usr/bin/python3
def uppercase(str):
    output = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            output += chr(ord(char) - 32)
        else:
            output += char
    print("{:s}".format(output))
