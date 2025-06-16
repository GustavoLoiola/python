val = []

for c in range(1,6):
    val.append(int(input(f'Digite o valor da {c}° posição: ')))
maior = max(val)
menor = min(val) 

print(f'Os valores digitados foram: {val}')
print(f'Os maiores valores digitados foram: {maior} na(s) posição(ões)', end=' ')
for i, v in enumerate(val):
    if v == maior:
        print(f'{i+ 1}...', end='')
print()
print(f'Os menores valores digitados foram: {menor} na(s) posição(ões)', end=' ')
for i, v in enumerate(val):
    if v == menor:
        print(f'{i+ 1}...', end='')
