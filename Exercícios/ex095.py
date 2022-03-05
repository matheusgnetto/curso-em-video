jogador = dict()
gols = list()
jogadores = list()
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print('=-=' * 20)
print(jogadores)
print('=-=' * 20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('---' * 15)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('---' * 15)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        break
    if dados >= len(jogadores):
        print(f'ERRO! Nao existe jogador com código {dados}')
    else:
        print(f' -- LEVANTAMENDO DO JOGADOR {jogadores[dados]["nome"].upper()}:')
        for k, i in enumerate(jogadores[dados]['gols']):
            print(f' => No jogo {k+1} fez {i} gols')
    print('---' * 15)
print('<< VOLTE SEMPRE >>')
