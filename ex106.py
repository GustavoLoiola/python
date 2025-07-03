def ajuda():
    """Sistema de ajuda com funções ou bibliotecas, digite o nome da """
    print('Sistema de ajuda PyHelp')
    while True:
        print('---'*45)
        perg = str(input('\033[32mFunção ou biblioteca [FIM para encerrar]: \033[m'))
        if perg.upper() == 'FIM':
            print('---'*45)
            print('\033[31mVolte sempre!\033[m')
            print('---'*45)
            break
        else:
            print('---'*45)
            print(f'\033[32mAcessando ao manual do comando {perg}...\033[m')
            print('---'*45)
            print('\033[1m')
            print(' ',end=' ')
            help(perg)
            print('\033[m')
        

ajuda()
