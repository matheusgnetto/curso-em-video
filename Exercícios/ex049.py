n = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 10+1):
    print('{} X {:2} = {}'.format(n, c, c*n))