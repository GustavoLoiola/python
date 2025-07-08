def LeiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mDados inválidos! Por favor, tente novamente!\033[m')
        else:
            break
        

def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    resposta = LeiaInt('Sua opção: ')
    return resposta
