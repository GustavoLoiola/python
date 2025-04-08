c = float(input('Digite uma termperatura em °C:'))
f = 1.8 * c + 32
k = c + 273
print('A temperatura °C{:.1f} equivale a °F{:.1f} e °K{:.1f}'.format(c, f, k))