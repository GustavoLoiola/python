lista = []
par = []
impar = []

while True:
    num = int(input('Digite um número para ser adicionado a lista: '))
    lista.append(num)
    qc = str(input('Quer continuar? [S/N]: ')).upper()
    if num % 2 ==0 and num != 0:
        par.append(num)
    if num == 0:
        print('0 é um número Nulo!')
    else:
        impar.append(num)
    if qc == 'N':
        break
print(f'Os números digitados foram: {lista}')
print(f'Os números PARES digitados foram {par}')
print(f'Os números ÍMPARES  digitados foram: {impar}')
