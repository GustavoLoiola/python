def LeiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mDados inválidos! Por favor, tente novamente!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número. Tente Novamente.\033[m')
            return 0
        else:
            return num
            
        
def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    resp = LeiaInt('\033[32mSua opção: \033[m')
    return resp
