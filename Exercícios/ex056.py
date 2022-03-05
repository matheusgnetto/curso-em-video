soma = 0
velho = 0
contmulher = 0
nomevelho = ''
for p in range(1, 5):
    print('-' * 4, '{}ª PESSOA'.format(p), '-' * 4)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip().upper())
    soma += idade
    if p == 1 and sexo == 'M':
        velho = idade
        nomevelho = nome
    if sexo == 'M' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        contmulher += 1

media = soma / 4
print('A media de idade do grupo é de {:.1f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(contmulher))
