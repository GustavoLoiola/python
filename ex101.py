def voto(ano):
    from datetime import date
    idade =  date.today().year - ano 
    if idade < 16:
        return print('NÃO VOTA!')
    elif idade >= 16 and idade < 18 or idade >= 70:
        return print('VOTO OPCIONAL!')
    elif idade >= 18 and idade < 70:
        return print('VOTO OBRIGATÓRIO!') 
ano_nas = int(input('Digite o seu ano de nascimento: '))
voto(ano_nas)
