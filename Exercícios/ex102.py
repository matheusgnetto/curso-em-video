def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c} x ', end='')
            if c == 2:
                print('1 = ', end='')
                break
    return f


# Programa principal
print(fatorial(7, show=True))
help(fatorial)
