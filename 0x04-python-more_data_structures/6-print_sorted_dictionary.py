#!/usr/bin/python3
def print_sorted_dictionary(d):
    if d:
        print('\n'.join(['{}: {}'.format(x, y) for x, y in sorted(d.items())]))
