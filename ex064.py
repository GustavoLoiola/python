num = 0
cont = -1
soma = -999
while num != 999:
    num = int(input('Digite um número [999 para parar.]: '))
    cont += 1
    soma += num
print('Você digitou {} números.'.format(cont))
print('A soma de todos os números foi igual a {}'.format(soma))
