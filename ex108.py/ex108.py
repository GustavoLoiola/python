import moeda

moeda.aumentar(20, 10)
moeda.diminuir(20,10)
moeda.dobro(20)
p = float(input('Valor: '))
met = moeda.metade(p)
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(met)}')
