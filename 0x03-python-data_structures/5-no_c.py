#!/usr/bin/python3
def no_c(my_string):
    return ''.join(str(a) for a in my_string if a is not 'c' and a is not 'C')
