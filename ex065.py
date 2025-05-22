mai = men = cont = tot = 0
qc = ' '

while qc != 'N':
    num = int(input('Digite um número: '))
    qc = str(input('Quer continuar? [S/N]: ')).upper()
    tot += num
    cont += 1
    if cont == 1:
        mai = num
        men = num
    else:
        if num > mai:
            mai = num

        if num < men:
            men = num
        
med = tot / cont
print('Você digitou {} números e a média entre eles foi {:.2f}'.format(cont, med))
print('O menor valor digitado foi {} e o maior valor digitado foi {}'.format(men, mai))
