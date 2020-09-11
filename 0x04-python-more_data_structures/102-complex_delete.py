#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i, j in dict(a_dictionary).items():
        if value in j:
            del a_dictionary[i]
    return a_dictionary
