s = float(input('Qual é o salário do funcionário? R$'))
if s <= 1250:
    novo = s + (s * 0.15)
else:
    novo = s + (s * 0.10)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s, novo))