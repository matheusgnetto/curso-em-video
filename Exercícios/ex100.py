from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        num = randint(1, 10)
        print(f'{num} ', end='')
        sleep(0.3)
        lista.append(num)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)

