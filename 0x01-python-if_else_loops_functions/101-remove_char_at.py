#!/usr/bin/python3
def remove_char_at(str, n):
    the_string = ""
    for s in range(len(str)):
        if s != n:
            the_string = the_string + str[s]
    return (the_string)
