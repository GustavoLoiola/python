from random import randint
numeros = list()
def sorteia(lista):
    for c in range(1,6):
        lista.append(randint(1,100))
    print(f'Sorteando 5 valores para lista: {lista} PRONTO!')


def somaPar(lista):
    pares = 0
    for cont in lista:
        if cont % 2 ==0:
            pares += cont
    print(f'Somando os valores pares de {lista}, temos: {pares}')


sorteia(numeros)
somaPar(numeros)
