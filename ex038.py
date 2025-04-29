n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número é maior ({:.2f} > {:.2f})'.format(n1, n2))

elif n2 > n1:
    print('O segundo número é maior ({:.2f} > {:.2f})'.format(n2, n1))

else:
    print('Não existe valor maior, os dois são iguais.')
