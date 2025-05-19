num = int(input('Digite um número para calcular o seu fatorial: '))
fat = 1
soma = 1
while fat <= num:
    soma *= fat
    fat += 1
print(soma)
