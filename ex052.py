soma = 0
cont = 0
num = int(input('Digite um número inteiro: '))

for c in range(1, (num+1)):
        soma += num
        cont += 1
if num % c ==0:
       print('O numero {} foi divisível {} vezes'.format(num, cont))

if cont == 2:
        print('O NÚMERO É PRIMO!')

else:
       ('O NÚMERO NÃO É PRIMO!')