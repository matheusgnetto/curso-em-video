print('===' * 9)
print('SUPER PROGRESSAO ARITMETICA')
print('===' * 9)

termo = int(input('Termo: '))
razao = int(input('Razao: '))
cont = 1
n = termo
while cont <= 10:
    print(n, '→', end=' ')
    n += razao
    cont += 1
print('Acabou')

more = int(input('Mostrar mais termos? Quantos? [N=0]: '))

while more != 0:
    cont = 1
    n = termo
    while cont <= 10 + more:
        print(n, '→', end=' ')
        n += razao
        cont += 1
    print('Acabou')
    more = int(input('Mostrar mais termos? Quantos? [N=0]: '))
print('Programa encerrado!')
