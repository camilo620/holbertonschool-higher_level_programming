#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    cont = 0
    for num in sys.argv[1:]:
        cont += int(num)
    print(cont)
