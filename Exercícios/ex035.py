print('-=' * 12)
print('Analisador de Triangulos')
print('-=' * 12)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Os segmentos acima PODEM FORMAR um triangulo!')
else:
    print('Os segmentos acima NAO PODEM formar um triangulo!')
