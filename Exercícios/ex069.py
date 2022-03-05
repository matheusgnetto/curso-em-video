cont = homem = mulher20 = 0
while True:
    print('---' * 10)
    print('     CADASTRE UMA PESSOA')
    print('---' * 10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('---' * 10)
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoa com mais de 18 anos: {cont}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher20} mulheres com menos de 20 anos.')
