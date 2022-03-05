from random import randint
print('=-=' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR, 1 A 10!')
print('=-=' * 10)
cont = s = 0
while True:
    c = randint(1, 10)
    n = int(input('Diga um valor: '))
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    s = c + n
    print(f'Voce jogou {n} e o computador {c}. Total de {s} ')
    if tipo == 'P' and s % 2 == 0:
        print('Voce GANHOU!')
        cont += 1
    elif tipo == 'I' and s % 2 != 0:
        print('Voce GANHOU!')
        cont += 1
    else:
        print('Voce PERDEU!')
        break
print(f'GAME OVER! Voce venceu {cont} vezes.')
