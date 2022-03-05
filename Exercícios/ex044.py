preco = float(input('Qual o valor da compra? '))
pgto = int(input('(0) dinheiro/cheque\n(1) cartao\n(2) 2x no cartao\n(3) 3x ou mais no cartao\n Qual a forma de pagamen'
                 'to? '))

if pgto == 0:
    desc = preco - (preco * 0.10)
    print('O preço final da compra fica em R${:.2f}.'.format(desc))
elif pgto == 1:
    desc = preco - (preco * 0.05)
    print('O preço final da compra fica em R${:.2f}.'.format(desc))
elif pgto == 2:
    parcela = preco / 2
    print('A compra será parcelada em 2x de R${:.2f} SEM JUROS!'.format(parcela))
    print('O preço final da compra fica em R${:.2f}'.format(preco))
elif pgto == 3:
    juros = preco + (preco * 0.20)
    parcelas = int(input('Quantas parcelas? '))
    final = juros / parcelas
    print('A compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(parcelas, final))
    print('O preço final da compra fica em R${:.2f}'.format(juros))
else:
    print('\033[1;31mOpçao inválida de pagamento. Tente novamente.\033[m')