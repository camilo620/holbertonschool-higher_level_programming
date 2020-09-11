#!/usr/bin/python3
def weight_average(my=[]):
    if my:
        return sum(tuple(i * j for i, j in my))/sum(n[1] for n in my)
    return 0
