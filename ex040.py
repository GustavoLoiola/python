n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
s = (n1 + n2) / 2
print('A soma entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2 , s))

if s >= 6:
    print('Você está aprovado, Parabéns!')

elif s >= 3:
    print('Você está de recuperação! Estude mais.')

else:
    print('Infelizmente, você foi reprovado!')
