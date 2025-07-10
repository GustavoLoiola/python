from menu import cadastro
from menu import arquivo

arq = 'cursoemvideo.txt'

if not arquivo.ArquivoExiste(arq):
    arquivo.CriarArquivo(arq)
cadastro.cabeçalho('SISTEMA DE GERENCIAMENTO DE PESSOAS')
while True:
    resposta = cadastro.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
    if resposta == 1:
        cadastro.cabeçalho('REGISTRO DE CADASTROS')
        arquivo.LerArquivo(arq)
    elif resposta == 2:
        cadastro.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = cadastro.LeiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        cadastro.cabeçalho('FIM DO SISTEMA!')
        print('\033[32mAté logo!\033[m')
        break
    else:
        print('\033[31mOpção inválida! Por favor tente novamente...\033[m')
