from datetime import date

ano = int(input('Ano de nascimento: '))

year = date.today().year
idade = year - ano
faltam = 18 - idade
passou = idade - 18

print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, year))
if idade < 18:
    print('Voce ainda irá se alistar no serviço militar. Faltam {} ano(s).\n Seu alistamento será em {}.'.format(
        faltam, year + faltam))
elif idade == 18:
    print('Este ano é seu alistamento no serviço militar!')
else:
    print('Já passou o tempo do seu alistamento militar. Foi há {} ano(s).\n Seu alistamento foi em {}'.format(
        passou, year - passou))
