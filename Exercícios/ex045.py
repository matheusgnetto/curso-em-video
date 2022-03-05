from random import randint
from time import sleep

print('\033[1;31m=-=\033[m' * 13)
print('\033[1;31m=-=\033[m' * 5, '\033[1;33mJOKENPO\033[m', '\033[1;31m=-=\033[m' * 5)
print('\033[1;31m=-=\033[m' * 13)
r = randint(0, 2)
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opçoes: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
op = int(input('Qual é a sua jogada? '))
print('JO'), sleep(0.5), print('KEN'), sleep(0.5), print('PO!!!')

print('\033[1;31m=-=\033[m' * 10)
print('Computador jogou {}'.format(itens[r]))
print('Jogador jogou {}'.format(itens[op]))
print('\033[1;31m=-=\033[m' * 10)

if r != op:
    if r == 0 and op == 1:
        print('JOGADOR VENCE!')
    elif r == 0 and op == 2:
        print('COMPUTADOR VENCE!')
    elif r == 1 and op == 0:
        print('COMPUTADOR VENCE!')
    elif r == 1 and op == 2:
        print('JOGADOR VENCE!')
    elif r == 2 and op == 0:
        print('JOGADOR VENCE!')
    elif r == 2 and op == 1:
        print('COMPUTADOR VENCE!')
    else:
        print('Jogada Inválida!')
else:
    print('EMPATE!')



