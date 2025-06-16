lista = []

while True:
    num = (int(input('Digite um valor para adicionar a lista: ')))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não será adicionado!')
    qc = str(input('Quer continuar? [S/N]: ')).upper()
    if qc == 'N':
        break
lista.sort()
print(f' Você digitou os seguintes valores {lista}')
