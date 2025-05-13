fra = str(input('Digite uma frase: ')).strip().upper()
palavra = fra.split()
junto = ''.join(palavra)
inverso = ''
print('Você digitou a frase {}'.format(junto))
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso é: {}'.format(inverso))
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase NÃO é um palíndromo!')
