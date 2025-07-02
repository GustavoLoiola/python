def leiaInt(num):
    """
    Função para validar se o conteúdo digitado é um número inteiro (num)."""
    while True:
        if num.isnumeric():
            print(f'Você acabou de digitar o número {num}')
            break
        else:
            print('\033[31mERRO! Você não digitou um número inteiro!\033[m')
            num = str(input('Digite outro número: '))


n = str(input('Digite um número: '))
leiaInt(n)
