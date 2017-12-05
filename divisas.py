# -*- coding: utf-8 -*- 

def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte dólares a soles.')
    print('')
    
    ammount = float(raw_input('Ingrese su monto en dolares: '))
    result = foreign_exchange_calculator(ammount)
    print('${} dólares equivalen a S/.{} nuevos soles.'.format(ammount, result))
    print('')

def foreign_exchange_calculator(ammount):
    dolar_to_soles_rate = 3.3
    return ammount * dolar_to_soles_rate

if __name__ == '__main__':
    run()