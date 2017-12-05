# -*- coding: utf-8 -*-

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

if __name__ == '__main__':
    n = int(raw_input('Ingrese número factorial: '))
    result = fact(n)
    print('El factorial de {} es: {} '.format(n, result))