from random import randint
from time import sleep
print('-_=' *57)
n = int(input('Tente advinhar o número entre 0 e 5 em que estou pensando: '))
pc = randint(0, 5)
print('PROCESSANDO...')
sleep(1)

if n == pc:
  print ('\033[1;32mParabéns, eu também pensei no número {}\033[m'.format(n))

elif n >= 6:
  print ('\033[1;45mEsse número é maior que 5 :(\033[m')

elif n <= -1:
  print ('\033[1;45mEsse número é negativo :(\033[m')

else:
  print ('\033[1;31mErrado! Eu pensei no número {}\033[m'.format(pc))
