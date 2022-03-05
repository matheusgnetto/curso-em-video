print('---' * 10)
print('      LOJA SUPER BARATAO')
print('---' * 10)
total = totMil = menor = contMenor = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    contMenor += 1
    total += preco
    if preco >= 1000:
        totMil += 1
    if contMenor == 1 or preco < menor:
        menor = preco
        barato = produto
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
