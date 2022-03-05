from time import sleep
x = 0
v1 = float(input('Valor 1: '))
v2 = float(input('Valor 2: '))
while x != 5:

    x = int(input('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    >>>>>> Opçao: '''))

    if x == 1:
        soma = v1 + v2
        print('Soma = {}'.format(soma))
    elif x == 2:
        mult = v1 * v2
        print('Multiplicaçao = {}'.format(mult))
    elif x == 3:
        if v1 > v2:
            print('Maior = {}'.format(v1))
        else:
            print('Maior = {}'.format(v2))
    elif x == 4:
        v1 = float(input('Valor 1: '))
        v2 = float(input('Valor 2: '))
    elif x == 5:
        print('Finalizando...')
    else:
        print('Opçao inválida, tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Programa finalizado!')