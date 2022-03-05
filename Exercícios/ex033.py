v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
if v1 < v2 and v1 < v3:
    menor = v1
else:
    if v2 < v1 and v2 < v3:
        menor = v2
    else:
        menor = v3
print('O menor valor digitado foi {}'.format(menor))
if v1 > v2 and v1 > v3:
    maior = v1
else:
    if v2 > v1 and v2 > v3:
        maior = v2
    else:
        maior = v3
print('O maior valor digitado foi {}'.format(maior))
