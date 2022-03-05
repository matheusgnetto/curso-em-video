lista = [[], []]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 != 0:
        lista[1].append(valor)
print('=-=' * 15)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')
