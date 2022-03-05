dados = dict()
pessoas = list()
soma = media = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while dados['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while c not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print(pessoas)
print('=-=' * 15)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estao acima da média: ', end='')
for p in pessoas:
    if p['idade'] > media:
        print(f'{p["nome"]} ', end='')
print()


