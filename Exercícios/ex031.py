d = float(input('Digite a distancia da sua viagem: '))
if d <= 200:
    preco = 0.50
else:
    preco = 0.45
total = d * preco
print('O preço da passagem por {}km é de R${:.2f}, ao total fica R${:.2f}.'.format(d, preco, total))