from random import randint
from time import sleep
r = randint(0, 5)
print('=-=-' * 14)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=-=-' * 14)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if n == r:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e nao no {}!'.format(r, n))



