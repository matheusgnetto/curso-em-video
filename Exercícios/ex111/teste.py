# EX111
# from ex111.utilidadesCeV import moeda
#
# p = float(input('Digite o preco: R$'))
# moeda.resumo(p, 35, 22)

# EX112
from ex111.utilidadesCeV import moeda, dados
p = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
