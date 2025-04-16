n = str(input('Digite seu nome: ')).strip()

print ('Seu nome maiúsulo é: {}'.format(n.upper()))
print ('Seu nome minúsculo é {}'.format(n.lower()))
print ('Seu nome possui {} letras'.format(len(n) - n.count(' ')))
print ('Seu primeiro nome possui {} letras'.format(n.find(" ")))
