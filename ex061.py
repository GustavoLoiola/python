print('---------- Progressão Aritmética ----------')
pt = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
num = 1
while num <= 10:
    print(pt, end=' -> ')
    pt += r
    num += 1
print('FIM')
