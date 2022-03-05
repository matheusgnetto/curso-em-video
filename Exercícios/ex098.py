from time import sleep


def linha():
    print('=-=' * 20)


def contador(i, f, p):
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont += p
        print('FIM')
    if i > f:
        cont = i
        while cont >= f:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont -= p
        print('FIM')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
