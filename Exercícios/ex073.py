tabela = ('atletico-mg', 'flamengo', 'palmeiras', 'fortaleza', 'corinthians', 'bragantino', 'fluminense', 'america-mg',
          'atletico-go', 'santos', 'ceara', 'internacional', 'sao paulo', 'atlhetico-pr', 'cuiaba', 'juventude',
          'gremio', 'bahia', 'sport', 'chapecoense')
print('=-=' * 5)
print(f'Lista de times do Brasileirao: {tabela}')
print('=-=' * 10)
print(f'Os 5 primeiros colocados sao {tabela[:5]}')
print('=-=' * 10)
print(f'Os 4 últimos colocados sao {tabela[-4:]}')
print('=-=' * 10)
print(f'Tabela em ordem alfabética: {sorted(tabela)}')
print('=-=' * 10)
print(f'A Chapecoense está na {tabela.index("chapecoense")+1} posiçao')
