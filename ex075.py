cont = val9 = p = val3 = 0

while cont <= 3:
    num = int(input('Digite um número: '))
    cont += 1
    if num == 9:
        val9 += 1
    elif num % 2 == 0 and num != 0:
        p += 1
    if num == 3:
        val3 +=1
        primeiro3 = cont
print(f'O valor 9 apareceu {val9} vezes.')
if val3 > 0:
    print(f'O valor 3 apareceu primeiro na {primeiro3}° posição.')
else:
    print('Não houveram ocorrências do valor 3.')
print(f'Foram digitados {p} números pares.')