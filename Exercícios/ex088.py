from random import randint
from time import sleep
lista = list()
jogos = list()
print('---' * 10)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('---' * 10)
j = int(input('Quantos jogos quer que eu sorteie?'))
tot = 1
while tot <= j:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('{:-^30}'.format(' SORTEANDO JOGOS '))
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('{:-^30}'.format(' BOA SORTE '))
