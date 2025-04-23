s = float(input('Digite o seu salário atual em R$: '))

if s <=1250.00:
  ns = s + (s*15/100)

else:
  ns = s + (s*10/100)

print('O seu novo salário é R${:.2f}'.format(ns))
