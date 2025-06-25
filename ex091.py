from random import randint
from time import sleep
from operator import itemgetter

ordem = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}

rank = list()
rank = sorted(ordem.items(), key= itemgetter(1), reverse= True)
print('SORTEADOR DE ORDEM DE DADOS!')
sleep(1)
print('+=' * 50)
for k, v in ordem.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.5)
print('+=' * 50)
print('A ordem ficou: ')
for i, v in enumerate(rank):
    print(f'{i +1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
