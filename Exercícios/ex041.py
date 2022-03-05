import datetime

ano = int(input('Digite o ano de nascimento do atleta: '))

year = datetime.date.today().year
idade = year - ano

print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria Mirim!')
elif idade <= 14:
    print('Categoria Infantil!')
elif idade <= 19:
    print('Categoria Junior!')
elif idade <= 25:
    print('Categoria Senior!')
else:
    print('Categoria Master!')