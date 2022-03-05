s = 0
cont = 0
for c in range(1, 6+1):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        cont += 1
        s += n
print('Voce digitou {} valores pares e a soma é igual a {}'.format(cont, s))


