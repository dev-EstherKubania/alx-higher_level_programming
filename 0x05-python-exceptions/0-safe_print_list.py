#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        the_count = 0
        for i in range(x):
            print(my_list[i], end="")
            the_count += 1
    except IndexError:
        pass
    finally:
        print()
        return the_count
