frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posiçao {}'.format(frase.find('A')+1))
print('A última letra A aparece na posiçao {}'.format(frase.rfind('A')+1))
