ficha = []
media = soma = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if c == 'N':
        break
print(ficha)
print('=-=' * 15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('---' * 10)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('=-=' * 15)
    opc = int(input('Mostar notas de qual aluno? [999 para parar] '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
