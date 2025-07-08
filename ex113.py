def LeiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mDados inválidos! Por favor, tente novamente!\033[m')
        else:
            print('Dados aceitos!')
            print('Volte Sempre, muito obrigado!')
            break


def LeiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except(ValueError, TypeError):
            print('Dados inválidos! Por favor, tente novamente!')
        else:
            print('Dados aceitos!')
            print('Volte sempre, muito obrigado!')
            break


LeiaInt('Digite um número inteiro: ')
LeiaFloat('Digite um número real: ')
