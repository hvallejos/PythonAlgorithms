# -*- coding: utf-8 -*-
import random

def run():
    number_found = False
    number_random = random.randint(0,20)
    print(number_random)
    while not number_found:
        number = int(raw_input('Ingrese el número: '))
        if number == number_random:
            print('Felicidades encontró el número.')
            number_found = True
        elif number < number_random:
            print('El número que busca es mayor')
        else:
            print('El número que busca es menor')
if __name__ == '__main__':
    run()