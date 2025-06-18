lista = [[[], [], []], [[], [], []], [[], [], []]]
conth = 0

while True:
    num = int(input(f'Digite um valor para [0:{conth}]: '))
    lista[0][conth].append(num)
    conth += 1
    if conth == 3:
        break
conth = 0
while True:
    num = int(input(f'Digite um valor para [1:{conth}]: '))
    lista[1][conth].append(num)
    conth += 1
    if conth == 3:
        break
conth = 0    
while True:
    num = int(input(f'Digite um valor para [2:{conth}]: '))
    lista[2][conth].append(num)
    conth += 1
    if conth == 3:
        break

print(lista[0])
print(lista[1])
print(lista[2])
