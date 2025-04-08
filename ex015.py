d = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos quilometros foram rodados?'))
t = d * 60 + km *0.15
print('O total a ser pago é de: {:.2f}'.format(t))