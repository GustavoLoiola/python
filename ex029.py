v = float(input('Qual a velocidade atual em KM? '))

if v >= 81:
      multa = (v-80) * 7
      print('MULTADO! Você excedeu o limite de 80Km/h')
      print('O valor da multa é: R${:.2f}'.format(multa))

else:
      print ('Tudo nos conformes!')
print ('Tenha um bom dia e dirija com segurança!')
    