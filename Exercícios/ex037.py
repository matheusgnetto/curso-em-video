n = int(input('Digite um número inteiro: '))
print('[ 1 ] para binário\n[ 2 ] para octal\n[ 3 ] para haxadecimal')
base = int(input('Qual será a base para conversao? '))

if base == 1:
    n = format(n, "b")
    print(n)
elif base == 2:
    n = format(n, "o")
    print(n)
elif base == 3:
    n = format(n, "x")
    print(n)
else:
    print('Opçao Inválida!')