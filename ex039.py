from datetime import date

nas = int(input('Digite o seu ano de nascimento: '))
id = date.today().year - nas
data = nas + 18

if id > 0 and id < 18:
    print ('Quem nasceu em {} possuí {} anos em {}'.format(nas, id, date.today().year))
    print('Você ainda não possuí idade para se alistar.')
    print('Você deverá se alistar em {}, daqui {} anos.'.format(data, data - date.today().year))

elif id == 18:
    print ('Quem nasceu em {} possuí {} anos em {}'.format(nas, id, date.today().year))
    print('Você deve se alistar ainda esse ano!')

elif id > 18 and id < 150:
    print ('Quem nasceu em {} possuí {} anos em {}'.format(nas, id, date.today().year))
    print('Você já deveria ter se alistado.')
    print('O ano do seu alistamento foi {}, {} anos atrás'.format(data, date.today().year - data))

else:
    print('Essa idade não condiz com a realidade.')
