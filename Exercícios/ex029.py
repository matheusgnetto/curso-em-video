v = float(input('Qual é a velocidade atual do carro? '))

if v > 80:
    print('MULTADO! Voce excedeu o limite permitido que é 80km/h'.format(v))
    multa = (v - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}.'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')

