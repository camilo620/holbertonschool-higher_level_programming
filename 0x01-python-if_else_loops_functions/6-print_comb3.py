#!/usr/bin/python3
for d in range(10):
    for d1 in range(d + 1, 10):
        if d != d1:
            if d == 8 and d1 == 9:
                print('{}{}'.format(d, d1))
            else:
                print('{}{}, '.format(d, d1), end='')
