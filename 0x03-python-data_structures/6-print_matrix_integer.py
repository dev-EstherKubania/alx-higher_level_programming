#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for p in range(len(matrix)):
        for k in range(len(matrix[p])):
            if k != 0:
                print(" ", end='')
            print("{:d}".format(matrix[p][k]), end='')
        print()
