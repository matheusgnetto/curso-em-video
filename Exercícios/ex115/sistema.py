from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opçao de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opçao de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opçao de sair do sistema.
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opçao errada no menu.
        print('\033[31mERRO! Digite uma opçao válida!\033[m')
    sleep(2)
