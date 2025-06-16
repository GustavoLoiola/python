lista = []
while True:
    num = int(input('Digite um valor para entrar na lista: '))
    lista.append(num)
    qc = str(input('Quer continuar? [S/N]: ')).upper()
    if qc == 'N':
        break 
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente foram: {lista}')
print(f'{len(lista)} números foram digitados.')

if 5 not in lista: 
    print('O número 5 NÃO está na lista!')
else:
     print('O número 5 ESTÁ na lista!')
