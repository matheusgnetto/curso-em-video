num = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in num:
        num.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if c == 'N':
        break
print('=-=' * 15)
num.sort()
print(f'Voce digitou os valores: {num}')


