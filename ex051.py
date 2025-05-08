print('=_-' * 58)
print('10 Primeiros termos de um razão de uma PA')

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite o valor da Razão: '))
for c in range (0, 10):
    print(pt + (c * r), end=' -> ')
print('ACABOU')
