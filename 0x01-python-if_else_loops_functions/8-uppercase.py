#!/usr/bin/python3
def uppercase(str):
    for u in str:
        if ord(u) >= ord('a') and ord(u) <= ord('z'):
            u = chr(ord(u) - 32)
        print('{:s}'.format(u), end='')
    print('')
