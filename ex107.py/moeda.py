def aumentar(num, porcentagem):
    """
    Calcula o acrèscimo de porcentagem de um determinado valor.
    num = número a ser usado.
    porcentagem = porcentagem que deverá ser adicionaada ao valor."""
    num += (num*porcentagem) / 100
    return num


def diminuir(num, porcentagem):
    """ Calcula o débito de porcentagem de um determinado valor.
    num = número a ser usado.
    porcentagem = porcentagem que deverá ser debitada ao valor."""
    num -= (num*porcentagem) / 100
    return num


def dobro(num):
    """Calcula o dobro de um valor.
    num = número a ser calculado."""
    num *= 2
    return num


def metade(num):
    """Calcula a metade de um valor.
    num = número a ser calculado."""
    num /= 2
    return num
