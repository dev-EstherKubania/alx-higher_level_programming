#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        the_count = 0
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                the_count += 1
        print()
        return the_count
    except IndexError:
        pass
