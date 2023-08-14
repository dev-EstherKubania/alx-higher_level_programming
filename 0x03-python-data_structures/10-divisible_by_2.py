#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [n % 2 == 0 for n in my_list]
    return new_list
