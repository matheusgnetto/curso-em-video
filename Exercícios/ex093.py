jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('=-=' * 20)
print(jogador)
print('=-=' * 20)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('=-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for k, i in enumerate(jogador['gols']):
    print(f'   => Na partida {k}, fez {i} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
