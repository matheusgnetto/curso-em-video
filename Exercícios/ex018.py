from math import sin, cos, tan, radians
a = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print('O angulo de {} tem o SENO de {:.2f}'.format(a, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(a, cosseno))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(a, tangente))