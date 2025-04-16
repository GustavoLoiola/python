import random
a1 = str(input('Primeiro nome: '))
a2 = str(input('Segundo nome: '))
a3 = str(input('Terceiro nome: '))
a4 = str(input('Quarto nome: '))
l = [a1, a2, a3, a4]
random.shuffle(l)
print('A ordem sorteada é: {}'.format(l))
