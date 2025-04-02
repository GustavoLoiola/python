la = float(input('Largura da parede:'))
al = float(input('Altura da parede:'))
ar = al * la
l = ar / 2
print('A área da parede é de {:.2f}M²'.format(ar))
print('Serão necessários {:.2f} litros de tinta para pintar a parede.'.format(l))