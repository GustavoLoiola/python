num = int(input('Digite um número inteiro para ver sua taboada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(c, num, (c * num)))
