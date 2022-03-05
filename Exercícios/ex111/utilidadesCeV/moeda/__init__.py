def metade(n, f=False):
    m = n / 2
    if f:
        return moeda(m)
    else:
        return m


def dobro(n, f=False):
    d = n * 2
    if f:
        return moeda(d)
    else:
        return n * 2


def aumentar(n, i=0, f=False):
    a = n + (n * (i/100))
    if f:
        return moeda(a)
    else:
        return n + (n * (i/100))


def diminuir(n, i=0, f=False):
    d = n - (n * (i / 100))
    if f:
        return moeda(d)
    else:
        return n - (n * (i/100))


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(n, a=0, r=0):
    print('---' * 10)
    print('RESUMO DO VALOR'.center(30))
    print('---' * 10)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{moeda(dobro(n))}')
    print(f'Metade do preço: \t{moeda(metade(n))}')
    print(f'{a}% de aumento: \t{moeda(aumentar(n, a))}')
    print(f'{r}% de reduçao: \t{moeda(diminuir(n, r))}')