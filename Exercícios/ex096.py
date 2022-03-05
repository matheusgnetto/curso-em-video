def areaTerreno(l, c):
    area = l * c
    print(f'A área de um terreno {l}x{c} é de {area}m2')


print(' Controle de Terrenos')
print('--' * 11)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
areaTerreno(l, c)

