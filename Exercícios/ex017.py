from math import hypot, sqrt
opt = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(sqrt(opt*opt + adj*adj))))