s = float(input('Digite o seu salário atual:'))
a = s + (s *15 /100)
print('O sálario de R${:.2f} passará a ser de R${:.2f} após o reajuste de 15%.'.format(s, a))