tent = 1
from random import randint
num = randint(0, 10)
print('TENTE ADVINHAR O NÚMERO EM QUE ESTOU PENSANDO [0, 10]:')
escolhido = int(input('Número: '))
while num != escolhido:
    print('ERRADO! Tente Novamente!')
    escolhido = int(input('Número: '))
    tent += 1

print('PARABÉNS!!! VOCÊ ACERTOU!')

if tent < 1:
    print('PARABÉNS, Você acertou de primeira!!!')

elif tent < 5:
    print('Você precisou de {} tentativas!'.format(tent))

else:
    print('Você demorou muito! precisou de {} tentativas!'.format(tent))
