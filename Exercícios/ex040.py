n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('\nMédia = {:.1f} \n\033[1:31mREPROVADO!\033[m'.format(media))
elif 5.0 <= media <= 6.9:
    print('\nMédia = {:.1f} \n\033[1:33mRECUPERAÇAO!\033[m'.format(media))
else:
    print('\nMédia = {:.1f} \n\033[1:32mAPROVADO!\033[m'.format(media))
