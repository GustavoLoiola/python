from datetime import date

info = dict()
info['Nome']= str(input('Nome: '))
ano = int(input('Data de nascimento: '))
info['Idade'] = date.today().year - ano
carteira= int(input('Número de registro da carteira de trabalho: '))
if carteira == 0:
    info['CPTS'] = 0
    for k, v in info.items():
        print(f'{k} tem o valor {v}')
else:
    info['Ano de contratação'] = int(input('Ano de contratação: '))
    info['Salário'] = float(input('Salário: '))
    info['Aposentadoria'] = 65 - info['Idade'] 
    for k, v in info.items():
        print(f'{k} tem o valor {v}')
