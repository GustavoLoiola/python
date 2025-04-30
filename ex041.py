from datetime import date
nas = int(input('Digite o seu ano de nascimento: '))
ano_atual = date.today().year 
idd = ano_atual - nas
print('O atleta tem {} anos.'.format(idd))

if idd <= 8:
    print('O atleta está na categoria: MIRIM.')

elif idd <= 13:
    print('O atleta está na categoria: INFANTIL.')

elif idd <= 18:
    print('O atleta está na categoria: JUNIOR.')

elif idd <= 24:
    print('O atleta está na categoria: SÊNIOR.')

else: 
    print('O atleta está na categoria: MASTER.')
