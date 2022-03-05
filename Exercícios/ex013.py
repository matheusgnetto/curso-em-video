salario = float(input('Digite o salário: '))
aumento = salario + (salario * 0.15)
print('O salário de R${:.2f}, com o aumento de 15% ficará em R${:.2f} .'.format(salario, aumento))