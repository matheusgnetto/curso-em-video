preco = float(input('Digite o preço do produto: R$'))
desc = preco - (preco * 0.05)
print('O produto com valor de R${:.2f}, com a promoçao de 5% de desconto ficará por R${:.2f}, aproveite!'.format(preco,
                                                                                                                 desc))