def area (alt, lar):
    a = alt * lar
    print(f'A área do Terreno é igual a {a:.2f}M²')


alt = float(input('Digite a altura: '))
lar = float(input('Digite a largura: '))


area(alt, lar)
