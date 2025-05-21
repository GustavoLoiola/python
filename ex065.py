mai = 0
men = 0
qc = ' '
cont = 0
tot = 0
while qc != 'N':
    num = int(input('Digite um número: '))
    qc = str(input('Quer continuar? [S/N]: ')).upper()
    tot += num
    cont += 1
med = tot / cont
if num > mai:
    mai = num
elif mai > men :
    men = num
print('Você digitou {} números e a média entre eles foi {:.0f}'.format(cont, med))
print('O menor valor digitado foi {} e o maior valor digitado foi {}'.format(men, mai))
