#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print('\n'.join([' '.join(['{:d}'.format(a) for a in i]) for i in matrix]))
