print('-------------------- LISTA DE COMPRAS --------------------')
mai = men = cont = soma = 0
nomemaiscaro = nomemaisbarato = ''
while True:
    pro = str(input('Nome do produto: '))
    val = float(input('Valor: '))
    qc = str(input('Quer continuar? [S/N]: ')).upper()
    soma += val
    cont += 1

    if qc == 'N':
        print('FIM DO PROGRAMA.')
        print(f'Você comprou {cont} produtos, e o total ficou em R${soma:.2f}')
        print(f'O produto mais caro foi o(a) {nomemaiscaro}, que custou  R${mai:.2f}')
        print(f'O produto mais barato foi o(a) {nomemaisbarato}, que custou R${men:.2f}')
        break


    elif cont == 1:
        mai = val
        men = val
        nomemaiscaro = pro
        nomemaisbarato = pro

    elif val > mai:
        mai = val
        nomemaiscaro = pro

    elif val < men:
        men = val
        nomemaisbarato = pro
