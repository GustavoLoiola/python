from menu import cadastro
cadastro.cabeçalho('SISTEMA DE CADASTRO')
while True:
    cadastro.cabeçalho('MENU PRINCIPAL')
    resposta = cadastro.menu(['Cadastrar nova pessoa', 'Ver pessoas cadastradas', 'Sair do programa'])
    if resposta == 1:
        print('OP1')
    if resposta == 2:
        print('OP2')
    if resposta == 3:
        print('FIM DO PROGRAMA!')
        print('Obrigado, volte sempre!')
        break
    else:
        print('ERRO! Por favor digite uma opção válida.')
