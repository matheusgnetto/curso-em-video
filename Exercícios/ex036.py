casa = int(input('Qual o valor da casa? R$'))
salario = int(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos ele vai pagar? '))

meses = anos * 12
mensal = casa / meses
limite = (salario + (salario * 0.30)) - salario

if mensal > limite:
    print('Empréstimo negado! A prestaçao mensal de R${:.2f} excede o valor de 30% (R${:.2f}) do salário de R${:.2f}'
          .format(mensal, limite, salario))
elif mensal < limite:
    print('Empréstimo aprovado! Prestaçao mensal de {:.2f} nao excede o valor de 30% (R${:.2f}) do salário de R${:.2f}'
          .format(mensal, limite, salario))
