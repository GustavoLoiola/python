Listagem = ('Lápis', 1.75,
            'Borracha', 2.10,
            'Estojo', 11.00,
            'Caneta', 2.00,
            'Garrafa', 14.50)
print('*'*40)
print('LISTA DE PREÇOS')
print('*'*40)
for pos in range(0, len(Listagem)):
    if pos % 2 ==0:
        print(f'{Listagem[pos]:.<30}', end='')
    else:
        print(f'R${Listagem[pos]:>7.2f}')
print('*'*40)