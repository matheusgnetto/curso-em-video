from datetime import date
year = date.today().year
maior = 0
menor = 0
for c in range(1, 7+1):
    nasc = int(input('Qual ano de nascimento da {} pessoa?: '.format(c)))
    idade = year - nasc
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('A quantidade de maiores de idade é de {} pessoas.'.format(maior))
print('A quantidade de menores de idade é de {} pessoas.'.format(menor))
