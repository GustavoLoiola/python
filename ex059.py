n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('---------- BEM VINDO AO MENU DE OPÇÕES ----------')
print(''' 
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR NÚMERO
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
op = int(input('OPÇÃO: '))

while op == 4:
    print('Informe os valores novamente.')
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print(''' 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NÚMERO
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    op = int(input('OPÇÃO: '))

if op == 1:
    print('{} + {} = {}'.format(n1, n2, (n1 + n2)))

elif op == 2: 
    print('{} x {} = {}'.format(n1, n2, (n1 * n2)))

elif op == 3:
    if n1 != n2:
        print('O maior número é {}.'.format(max(n1, n2)))

    else:
        print('Os dois valores são iguais.')

while op not in range(1, 6):
    print('OPÇÃO INVÁLIDA! Tente Novamente.')
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print('---------- BEM VINDO AO MENU DE OPÇÕES ----------')
    print(''' 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NÚMERO
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    op = int(input('OPÇÃO: '))
