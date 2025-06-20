par = coluna3 = linha2 = 0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = num = int(input(f'Digite um valor para [{l}]:[{c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            coluna3 +=  num
        if l == 1:
            linha2 += num
print('=-' * 50)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print(f'A soma de todos os números pares resultou em {par}')
print(f'A soma dos valores da terceira coluna resultou em {coluna3}.')
print(f'A soma dos valores da segunda linha resultou em {linha2}.')
