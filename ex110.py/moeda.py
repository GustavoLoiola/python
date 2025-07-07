def moeda(num=0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')


def aumentar(num, porcentagem, formato=False):
    """
    Calcula o acrèscimo de porcentagem de um determinado valor.
    num = número a ser usado.
    porcentagem = porcentagem que deverá ser adicionaada ao valor.
    formato=True = opção para fazer a formatação em moeda (R$xx,xx), False é o valor padrão e não faz a formatação. """
    num += (num*porcentagem) / 100
    return num if format == False else moeda(num)


def diminuir(num, porcentagem, formato=False):
    """ Calcula o débito de porcentagem de um determinado valor.
    num = número a ser usado.
    porcentagem = porcentagem que deverá ser debitada ao valor.
    formato=True = opção para fazer a formatação em moeda (R$xx,xx), False é o valor padrão e não faz a formatação."""
    num -= (num*porcentagem) / 100
    return num if format == False else moeda(num)


def dobro(num=0, formato=False):
    """Calcula o dobro de um valor.
    num = número a ser calculado.
    formato=True = opção para fazer a formatação em moeda (R$xx,xx), False é o valor padrão e não faz a formatação."""
    num *= 2
    return num if format == False else moeda(num)


def metade(num=0, formato=False):
    """Calcula a metade de um valor.
    num = número a ser calculado.
    formato=True = opção para fazer a formatação em moeda (R$xx,xx), False é o valor padrão e não faz a formatação."""
    num /= 2
    return num if format == False else moeda(num)


def resumo(num, aumento, redução):
    """Faz um resumo de aumento de porcentagem, redução de porcentagem, dobro e metade do valor.
    num = número a ser analisado.
    aumento = porcentagem a ser adicionada ao valor.
    redução = porcentagem a ser reduzida do valor."""
    import moeda
    print('-' * 36)
    print('RESUMO'.center(36))
    print('-' *36)
    dobro = moeda.dobro(num)
    metade = moeda.metade(num)
    aumentar = moeda.aumentar(num, aumento)
    diminuir = moeda.diminuir(num, redução)
    print(f'Resumo do valor:      {num}')
    print(f'{aumento}% de aumento:       {aumentar}')
    print(f'{redução}% de redução:       {diminuir}')
    print(f'dobro do preço:       {dobro}')
    print(f'Metade do preço:      {metade}')
    print('-' * 36)
