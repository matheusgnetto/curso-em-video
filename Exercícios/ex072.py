cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# num = int(input('Digite um numero entre 0 e 20: '))
# while num < 0 or num > 20:
#     print('Tente novamente. ')
#     num = int(input('Digite um numero entre 0 e 20: '))
# print(f'Voce digitou o número {cont[num]}')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        print('Tente novamente. ', end='')
        num = int(input('Digite um número entre 0 e 20: '))
    print(f'Voce digitou o número {cont[num]}')
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print('Programa finalizado!')

