dic = dict()
dic['Nome'] = str(input('Nome: '))
dic['Média'] = float(input(f'Média de {dic["Nome"]}:'))
if dic['Média'] < 6:
    dic['Situaçao'] = 'Reprovado'
elif dic['Média'] < 7:
    dic['Situaçao'] = 'Recuperaçao'
else:
    dic['Situaçao'] = 'Aprovado'
for k, v in dic.items():
    print(f'{k} é igual a {v}')



