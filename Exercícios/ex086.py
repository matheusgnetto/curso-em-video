# matriz = []
# dados = []
#
# for i in range(0, 3):
#     for c in range(0, 3):
#         dados.append(int(input(f'Digite um valor para [{i}, {c}]: ')))
#     matriz.append(dados[:])
#     dados.clear()
#
# print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]')
# print(f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]')
# print(f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')

matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()