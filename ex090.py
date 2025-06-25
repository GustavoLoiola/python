aluno = dict()

nome_aluno = str(input('Nome do aluno: '))
nota = float(input('Média do aluno: '))
aluno['Nome: '] = nome_aluno
aluno['Média: '] = nota

if nota >= 7:
    aluno['Situação:'] = 'APROVADO'
elif nota >= 4:
    aluno['Situação:'] = 'RECUPERAÇÃO'
else:
    aluno['Situação:'] = 'REPROVADO'
print(f'{'Nome'} é igual a {nome_aluno}')
print(f'{'Média'} é igual a {nota}')
print(f'{'Situação'} é igual a {aluno["Situação:"]}')
