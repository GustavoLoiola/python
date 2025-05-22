p = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if c % 2 == 0:
        p +=1
print('{} números são pares.'.format(p))
