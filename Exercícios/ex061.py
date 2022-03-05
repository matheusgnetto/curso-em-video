print('===' * 7)
print('10 TERMOS DE UMA PA')
print('===' * 7)

termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
cont = 1
while cont <= 10:
    print(termo, '→', end=' ')
    termo += razao
    cont += 1
print('Acabou')
