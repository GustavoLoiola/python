print('CALCULADORA DE IMC')
p = float(input('Digite o seu peso (Kg): '))
a = float(input('Digite a sua altura (m): '))
indice = p / (a * a)

print('O seu IMC atual é de: {:.2f}'.format(indice))
      
if indice <18.5 and indice > 0:
    print('Você está abaixo do peso ideal, Cuidado!')

elif indice < 25:
    print('Parabéns, você está no peso Ideal!')

elif indice < 30:
    print('Você está com Sobrepeso.')

elif indice < 40:
    print('Você está com Obesidade, Cuidado!')

elif indice > 40:
    print('Você está com Obesidade Mórbida, MUITO CUIDADO!')

else:
    print('Os valores digitados não são reais.')
