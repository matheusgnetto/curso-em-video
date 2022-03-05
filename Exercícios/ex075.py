num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o ultimo número: ')))

print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posiçao')
else:
    print('Nao foi encontrado nenhum valor 3')
print('Os valores pares digitados foram ', end='')
for v in num:
    if v % 2 == 0:
        print(v, end=' ')
