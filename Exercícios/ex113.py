def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido!\033[m')
        except KeyboardInterrupt:
            print('Usuário preferiu nao digitar este número.')
            return 0
        else:
            return r


# Programa principal
n = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real:')
print(f'O valor inteiro digitado foi {n} e o valor real {r}')