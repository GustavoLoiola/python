num = int(input("Digite um número: "))
contador = 0

for c in range(1, num + 1):
    if num % c == 0:
        contador += 1

print("O número {} foi divisível {} vezes!".format(num, contador))
if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")
