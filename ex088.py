from random import randint
from time import sleep

jogos = []
numeros = []
tot = 0
print('-='*50)
print('SORTEADOR MEGA-SENA')
print('-='*50)
vezes = int(input('Quantos jogos você quer sortear? '))

while tot < vezes:
    cont = 0
    while True:
       num = randint(1,60)
       if num not in numeros:
           numeros.append(num)
           cont += 1
       if cont >= 6:
           break
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    tot += 1
print(f'SORTEANDO {vezes} JOGOS')
for i, l in enumerate(jogos):
    print(f'JOGO {i+1}: {l}')
    sleep(1)
