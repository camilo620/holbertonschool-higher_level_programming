#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    cont = len(sys.argv[1:])
    if cont == 0:
        print('0 arguments.')
    elif cont == 1:
        print('1 argument:\n1: {}'.format(sys.argv[1]))
    else:
        print('{} arguments:'.format(cont))
        cont = 1
        for arg in sys.argv[1:]:
            print('{}: {}'.format(cont, arg))
            cont += 1
