#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if 97 <= ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
