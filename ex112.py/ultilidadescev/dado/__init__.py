def leiadinheiro(msg):
    """Faz uma validação de um valor monetário.
    msg = valor"""
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha():
            print(f'\033[31mERRO: "{entrada}" é um valor inválido!\033[m')
        else:
            válido = True
            return float(entrada)
