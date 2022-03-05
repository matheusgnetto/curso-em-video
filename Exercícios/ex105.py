def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e situaçoes da varios alunos
    :param n: Uma ou mais notas dos alunos (aceita varias).
    :param sit: valor opcional, indicando se deve ou nao a situaçao.
    :return: Dicionário com várias informaçoes sobre a situaçao da turma.
    """
    tot = dict()
    tot['total'] = len(n)
    tot['maior'] = max(n)
    tot['menor'] = min(n)
    tot['media'] = sum(n) / len(n)
    if sit:
        if tot['media'] >= 7:
            tot['sit'] = 'boa'
        elif tot['media'] >= 5:
            tot['sit'] = 'razoavel'
        else:
            tot['sit'] = 'ruim'
    return tot


# Programa principal
resp = notas(5.5, 2.5, 8.5)
help(notas)
