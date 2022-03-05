from datetime import date


def voto(i=0):
    if i < 16:
        return 'VOTO NEGADO'
    elif 16 <= i < 18 or i > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'


ano = int(input('Em que ano voce nasceu? '))
idade = date.today().year - ano
print(f'Com {idade} anos: {voto(idade)}')
