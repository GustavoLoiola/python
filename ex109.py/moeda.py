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


