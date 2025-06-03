num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')),
       )


print(f'Você digitou o valor 9 {num.count(9)} vezes.')
print(f'O valor 3 apareceu inicialmete na {num.index(3) + 1} posição.')
print('Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
