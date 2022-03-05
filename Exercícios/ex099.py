from time import sleep


def linha():
    print('=-=' * 20)


def maior(* maior):
    linha()
    print('Analisando valores passados...')
    cont = m = 0
    for num in maior:
        print(f'{num} ', end='')
        sleep(0.5)
        if cont == 0:
            m = num
        else:
            if num > m:
                m = num
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


maior(3, 5, 8, 2, 1)
maior(2, 5, 6)
maior(9, 1)
maior(5)
maior()
