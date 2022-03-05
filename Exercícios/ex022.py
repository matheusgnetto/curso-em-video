nome = str(input('Digite seu nome: ')).strip()
nome1 = nome.split()
contar = nome.replace(" ", "")
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(contar)))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome1[0], len(nome1[0])))

