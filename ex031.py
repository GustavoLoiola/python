km = float(input('Digite a quantidade de Km da viagem: '))
if km <=200:
    r1= km * 0.50
    print('O valor da viagem é R${:.2f}'.format(r1))

else:
    r1= km * 0.45
    print('O valor da viagem é R${:.2f}'.format(r1))
