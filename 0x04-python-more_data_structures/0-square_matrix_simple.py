#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = []
        for rows in matrix:
            new_matrix.append(list(map(lambda x: x**2, rows)))
        return (new_matrix)
    return None
