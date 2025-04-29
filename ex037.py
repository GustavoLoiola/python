import math
n = int(input('Digite um número inteiro: '))
opcao = int(input("""Digite [1] para converter para binário.
Digite [2] para converter para Octal.
Digite [3] para converter para Hexadecimal.
Número escolhido: """))

if opcao == 1:
    print('O número {} corresponde a {} em Binário.'.format(n, bin(n)))

elif opcao == 2:
    print('O número {} corresponde a {} na base Octal.'.format(n, oct(n)))

elif opcao == 3:
    print('O número {} corresponde a {} em Hexadecimal.'.format(n, hex(n)))

else:
    print('\033[31mNúmero inválido!\033[m')
