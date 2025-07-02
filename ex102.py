def fatorial(num, show=False):
    """ Calcula o fatorial de um número inteiro.
    num = número para visualização do fatorial
    show(opcional) = para visualização do cálculo fatorial
    """
    fat = 1
    soma = 1
    while fat <= num:
        soma *= fat
        fat += 1 
    if show == True:
        for c in range(num, 0, -1):
            print(f'{c}', end='')
            if c > 1:
               print(' x ', end='')
            else:
               print(' = ', end='')
    print(soma)
   


numero = int(input('Digite um número para ver o seu fatorial: '))
fatorial(numero, show=True)
help(fatorial)
