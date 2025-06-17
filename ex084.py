temp = []
princ = []

while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    qc = str(input('Quer continuar? [S/N]: ')).upper()
    if qc == 'N':
        print('FIM')
        break

print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'A pessoa mais pesada tem {maior:.2f}Kg e se chama', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'A pessoa mais leve tem {menor:.2f}Kg e se chama', end=' ')
for p in princ:
    if p[1] == menor:
            print(f'{p[0]}')
