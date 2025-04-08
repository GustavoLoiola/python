c = float(input('Digite uma termperatura em °C:'))
f = 1.8 * c + 32
k = c + 273
print('A temperatura {:.1f}°C equivale a {:.1f}°F e {:.1f}°K'.format(c, f, k))