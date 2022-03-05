num = cont = soma = maior = menor = 0
opt = ''
while opt in 'Ss':
    num = int(input('Digite um número: '))
    opt = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media = soma / cont
print('Voce digitou {} numeros e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

