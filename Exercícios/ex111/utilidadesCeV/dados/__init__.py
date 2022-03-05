def leiaDinheiro(msg):
    valido = False
    valor = 0
    while not valido:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[31mERRO: {n} é um preço inválido!\033[m')
        else:
            valido = True
            return float(n)
