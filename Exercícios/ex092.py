from datetime import datetime
dic = dict()
dic['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dic['idade'] = datetime.now().year - nasc
dic['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if dic['ctps'] != 0:
    dic['contrataçao'] = int(input('Ano de Contrataçao: '))
    dic['salario'] = float(input('Salário: '))
    dic['aposentadoria'] = dic['idade'] + (dic['contrataçao'] + 35 - datetime.now().year)
print('=-=' * 15)
for k, v in dic.items():
    print(f'  - {k} tem o valor {v}')
