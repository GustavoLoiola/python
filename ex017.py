from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A Hipotenusa vale: {:.2f}'.format(hi))