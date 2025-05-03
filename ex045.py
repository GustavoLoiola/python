from random import randint
from time import sleep

print('=_-' * 57)
print('Vamos jogar Pedra Papel Tesoura!')

print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')

op = int(input('SUA ESCOLHA: '))

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)

print('VOCÊ ESCOLHEU: {}'.format(itens[op]))
print('MINHA ESCOLHA: {}'.format(itens[computador]))

if op ==  computador:
    print('EMPATE')

elif op == 0 and computador == 2:
    print('VOCÊ GANHOU!')

elif op == 0 and computador == 1:
    print('VOCÊ PERDEU!')

elif op == 1 and computador == 0:
    print('VOCÊ GANHOU!')

elif op == 1 and computador == 2:
     print('VOCÊ PERDEU!')

elif op == 2 and computador == 1:
     print('VOCÊ GANHOU!')

elif op == 2 and computador == 0:
    print('VOCÊ PERDEU!')

else:
    print('Número inválido!')
