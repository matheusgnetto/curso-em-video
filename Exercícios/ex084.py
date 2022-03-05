pessoa = []
dados = []
pmenor = pmaior = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoa) == 0:
        pmaior = pmenor = dados[1]
    else:
        if dados[1] > pmaior:
            pmaior = dados[1]
        if dados[1] < pmenor:
            pmenor = dados[1]
    pessoa.append(dados[:])
    dados.clear()
    ctn = ' '
    while ctn not in 'SN':
        ctn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if ctn == 'N':
        break
print(f'Ao todo voce cadastrou {len(pessoa)} pessoas.')
print(f'O maior peso foi de {pmaior}Kg. Peso de', end=' ')
for p in pessoa:
    if p[1] == pmaior:
        print(f'{p[0]}')
print(f'O menor peso foi de {pmenor}Kg. Peso de', end=' ')
for p in pessoa:
    if p[1] == pmenor:
        print(f'{p[0]}')
