sexo = str(input('Digite o sexo: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Valor inválido! Digite novamente: ')).strip().upper()[0]
print('Sexo registrado com sucesso!')