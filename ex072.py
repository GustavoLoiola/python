nome = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20 para ver a sua escrita por extenso: '))
    if num < 0 or num > 20:
        print('Número inválido!')
    if num > 0 and num < 21:
            break
print(f'Você digitou o número: {nome[num]}')
