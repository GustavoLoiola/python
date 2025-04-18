a = str(input('Digite o seu nome completo: ')).upper().strip()
print ('A letra "A" aparece em seu nome {} vezes'.format(a.count('A')))
print ('A letra "A" aparece pela primeira vez na posição {}'.format(a.find('A')+1))
print ('A letra "A" aparece pela última vez na posição {}'.format(a.rfind('A')+1))
