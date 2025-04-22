from random import randint
from time import sleep
print('-_=' *40)
n = int(input('Tente advinhar o número entre 0 e 5 em que estou pensando: '))
pc = randint(0, 5)
print('PROCESSANDO...')
sleep(2)

if n == pc:
  print ('Parabéns, eu também pensei no número {}'.format(n))

elif n >= 6:
  print ('Esse número é maior que 5 :(')

elif n <= 0:
  print ('Esse número é negativo :(')

else:
  print ('Errado! Eu pensei no número {}'.format(pc))
