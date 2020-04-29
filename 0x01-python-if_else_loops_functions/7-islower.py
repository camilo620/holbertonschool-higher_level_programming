#!/usr/bin/python3
def islower(c):
    for l in range(ord('a'), ord('z') + 1):
        if ord(c) == l:
            return True
    else:
        return False
