print('--------------- CADASTRO DE PESSOAS ---------------')
midd = hom = iddmul = mulmen21 = 0
while True:
    nom = str(input('Nome: '))
    idd = int(input('Idade: '))
    sex = str(input('Sexo [F/M]: ')).upper()
    print('-'*50)
    qc = str(input('Quer cadastrar mais alguém? [S/N]: ')).upper()

    if idd >= 18: 
        midd += 1

    if sex == 'M':
        hom += 1

    if sex == 'F':
        iddmul += idd
        if iddmul <= 20:
            mulmen21 += 1

    if qc == 'N':
        print('FIM DE CADASTRO')
        print(f'{midd} Pessoas são maiores de idade.')
        print(f'{hom} Homens foram cadastrados.')
        print(f'{mulmen21} Mulheres são menores de 21 anos.')
        break
