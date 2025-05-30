from random import randint
pc = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
for p in pc:
    print(f'{p}', end=' ')
print('Foram os números sorteados.')
print(f'O maior valor sorteado foi: {(max(pc))}')
print(f'O Menor valor sorteado foi: {(min(pc))}')
