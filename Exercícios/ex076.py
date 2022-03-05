listagem = ('Pao', 1,
            'Leite', 3.50,
            'Arroz', 7,
            'Feijao', 11,
            'Café', 18.90)

print('---' * 20)
print('{:^60}'.format('LISTAGEM DE PREÇOS'))
print('---' * 20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>8.2f}')
print('---' * 20)



