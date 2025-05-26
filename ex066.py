cont = s = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    s += num
    cont += 1
print(f'Você digitou {cont} números e a soma deles resultou em {s}.')
