l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
area = l * a
tinta = area / 2
print('Sua parede tem a dimensao de {:.1f}x{:.2f} e sua área é de {:.3f}m².\n'
      'A quantidade de tinta necessária para pintar está parede é de {:.4f}l de tinta.'.format(l, a, area, tinta))