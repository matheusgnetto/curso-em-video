matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
somapar = soma = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 1:
            maior = matriz[l][0]
            if matriz[l][c] > maior:
                maior = matriz[l][c]
    print()
print('=-=' * 15)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')


