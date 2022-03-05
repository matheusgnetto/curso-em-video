palavras = ('atender', 'maestro', 'roupa', 'camisa', 'aviao', 'estojo', 'papel', 'banana')
for v in palavras:
    print(f'\nNa palavra {v.upper()} temos ', end='')
    for letra in v:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
