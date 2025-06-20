lista = [[], []]
notas = [[], []]
cont = tot = 0
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    lista[0].append(nome)
    lista[1].append(media)
    notas[0].append(nota1)
    notas[1].append(nota2)
    cont += 1
    qc = str(input('Quer continuar? [S/N]: ')).upper()
    if qc == 'N':
        break

for c in range(cont):
    print(f'ALUNO: {lista[0][tot]}/ MÉDIA: {lista[1][tot]:.2f}')
    tot += 1

for c in range(tot):
    print(f'[{c}] = {lista[0][c]}')
while True: 
    print('De qual aluno você deseja ver as notas? [999 para parar]')
    nota_aluno = int(input('ALUNO: '))
    if nota_aluno == 999:
        print('Volte Sempre!')
        break
    else:
        print(f'Primeira nota de {lista[0][nota_aluno]}: {notas[0][nota_aluno]:.2f}')
        print(f'Segunda nota de {lista[0][nota_aluno]}: {notas[1][nota_aluno]:.2f}')
