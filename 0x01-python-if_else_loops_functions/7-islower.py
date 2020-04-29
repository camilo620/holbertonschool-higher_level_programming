#!/usr/bin/python3
def lower(i):
    for l in range(ord('a'), ord('z') + 1):
        if ord(i) == l:
            return True
    else:
        return False
