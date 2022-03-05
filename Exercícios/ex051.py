print('===' * 10)
print('10 TERMOS DE UMA PA')
print('===' * 10)

termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = termo + (10-1) * razao
for n in range(termo, decimo + razao, razao):
    print(n, '→', end=' ')
print('Acabou')

