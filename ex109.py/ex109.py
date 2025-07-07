import moeda

p = float(input('Valor: '))
mais = moeda.aumentar(p, 10, True)
moeda.diminuir(p, 10)
moeda.dobro(p)
met = moeda.metade(p)
print(mais)
