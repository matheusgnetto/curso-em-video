from random import randint
print('=-=' * 20, '\n Vou pensar em um número entre 0 e 10. Tente adivinhar...\n', '=-=' * 20)
computador = randint(0, 10)
num = int(input('Em que número eu pensei? '))

cont = 0
while num != computador:
    cont += 1
    if num < computador:
        print('Mais... Tente mais uma vez.')
        num = int(input('Em que numero eu pensei? '))
    elif num > computador:
        print('Menos... Tente mais uma vez.')
        num = int(input('Em que numero eu pensei? '))
print('PARABENS! Acertou após {} tentativas!'.format(computador, cont))
